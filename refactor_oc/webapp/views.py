from webapp.models import Rating, Participant
from django.views.generic import DetailView, ListView, View, DeleteView
from django.shortcuts import render, render_to_response
from webapp.models import Bestseller, Movie, Person, Bookmark, Comment, Genre, Selection, OCUser
from django.views.generic.base import TemplateView
import json
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


class AjaxSearchView(TemplateView):
    template_name = 'ajax_search.html'

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        movie = Movie.objects.all()
        person = Person.objects.all()

        context = {
            'movies': movie.filter(Q(name__icontains=q) | Q(international_name__icontains=q))[:3],
            'persons': person.filter(Q(name__icontains=q) | Q(international_name__icontains=q))[:3]
        }

        return context


# Конец


# Результаты поиска
class SearchListView(TemplateView):
    template_name = 'search_list.html'

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        movie = Movie.objects.filter(Q(name__icontains=q) | Q(international_name__icontains=q)).order_by('pk')
        person = Person.objects.filter(Q(name__icontains=q) | Q(international_name__icontains=q)).order_by('pk')

        # Пагинация для фильмов
        paginator = Paginator(movie, 6)
        page_number = self.request.GET.get('page', 1)
        movie = paginator.get_page(page_number)

        # Пагинация для актёров
        paginator = Paginator(person, 6)
        page_number = self.request.GET.get('page', 1)
        person = paginator.get_page(page_number)

        context = {
            'search_input': q,
            'movies': movie,
            'persons': person
        }

        return context


# Конец


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['bookmark'] = Bookmark.objects.filter(user=self.request.user, movie=self.object)
        context['producers'] = Participant.objects.filter(movie=self.object, role_id=1)
        context['actors'] = Participant.objects.filter(movie=self.object, role_id=3)
        context['comments'] = Comment.objects.filter(movies=self.object).order_by('-created_at')[:10]
        context['comments_len'] = len(Comment.objects.filter(movies=self.object))
        if self.object.group:
            context['compilation'] = Movie.objects.filter(group=self.object.group)
        else:
            context['compilation'] = self.get_compilation_by_genres(
                Genre.objects.filter(movies__in=[self.object.movie_id]))
        return context

    @staticmethod
    def get_compilation_by_genres(genres):
        res = []
        for i in genres:
            res.append(i.genre_id)
        if len(res) > 2:
            return Movie.objects.filter(genres__in=res[:3]).order_by("?")[:5]
        else:
            return Movie.objects.filter(genres__in=res).order_by("?")[:5]


class ActorDetailView(DetailView):
    model = Person
    template_name = 'actor.html'


class FavoritesListView(ListView):
    model = Bookmark
    template_name = 'favorite_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        success_url = reverse('webauth:signup')
        context['movies'] = self.model.objects.filter(user=self.request.user).order_by('-created_at')
        return context


class BestsellerListView(ListView):
    model = Bestseller
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['movie_all'] = []
        classes = {
            1: 'fa-angellist',
            2: 'fa-smile-o',
            3: 'fa-bomb',
            4: 'fa-video-camera',
            5: 'fa-cloud',
            6: 'fa-bug',
            7: 'fa-meh-o',
            8: 'fa-magic',
            9: 'fa-heart',
            10: 'fa-user-secret'
        }
        for bestseller in Bestseller.objects.all():
            movies_str = bestseller.movies
            movie_list = json.loads(movies_str)
            q = {
                'category': bestseller.name,
                'movies': [],
                'classname': classes[bestseller.category_id]
            }
            for i in movie_list:
                q['movies'].append(Movie.objects.get(movie_id=i))
            context['movie_all'].append(q)
        return context


class CatalogueListView(ListView):
    model = Movie
    template_name = 'catalogue.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogueListView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-created_at')[:5]
        all_movies = Movie.objects.all().order_by('-created_at')
        context['paginator'] = Paginator(all_movies, 20)
        context['page'] = self.request.GET.get('page')
        context['movies'] = context['paginator'].get_page(context['page'])
        return context


class MovieView(DetailView):
    model = Movie
    template_name = 'view_movie.html'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        request_comments = []
        comments = Comment.objects.filter(movies=self.object, to_comment__comment_id__isnull=True).order_by(
            '-created_at')
        for comment in comments:
            request_comments.append(comment)
        context['comments'] = request_comments
        if len(context['comments']) > 4:
            context['comments_len'] = len(context['comments']) - 4
        if self.request.user.is_authenticated:
            context['bookmark'] = Bookmark.objects.filter(user=self.request.user, movie=self.object)
        context['comments'] = Comment.objects.filter(movies=self.object, to_comment__comment_id__isnull=True).order_by('-created_at')[:10]
        context['comments_len'] = len(Comment.objects.filter(movies=self.object))
        if self.object.group:
            context['compilation'] = Movie.objects.filter(group=self.object.group)
        else:
            context['compilation'] = self.get_compilation_by_genres(
                Genre.objects.filter(movies__in=[self.object.movie_id]))
        return context

    @staticmethod
    def get_compilation_by_genres(genres):
        res = []
        for i in genres:
            res.append(i.genre_id)
        if len(res) > 2:
            return Movie.objects.filter(genres__in=res[:3]).order_by("?")[:5]
        else:
            return Movie.objects.filter(genres__in=res).order_by("?")[:5]


class CommentCreateView(View):
    model = Comment
    template_name = 'view_movie.html'

    def post(self, request, *args, **kwargs):
        movie_id = self.request.POST.get('movie_id')
        text = self.request.POST.get('text')
        user_pk = self.request.POST.get('user_pk')
        csrft = self.request.POST.get('csrfmiddlewaretoken')
        print(csrft)
        user = OCUser.objects.get(pk=user_pk)
        movie = Movie.objects.get(movie_id=movie_id)
        new_comment = movie.comments.create(user=user, text=text)
        comment = [{'user': new_comment.user.login, 'text': new_comment.text, 'created_at': new_comment.created_at.
            strftime('%-d %b %Y %H:%M'), 'comment_id': new_comment.comment_id}]
        return JsonResponse(comment, safe=False)


class CommentAnswerView(View):
    model = Comment
    template_name = 'view_movie.html'

    def post(self, request, *args, **kwargs):
        movie_id = self.request.POST.get('movie_id')
        text = self.request.POST.get('text')
        user_pk = self.request.POST.get('user_pk')
        to_comment_id = self.request.POST.get('to_comment_id')
        user = OCUser.objects.get(pk=user_pk)
        movie = Movie.objects.get(movie_id=movie_id)
        new_comment = movie.comments.create(user=user, text=text, to_comment_id=to_comment_id)
        comment = [{'user': new_comment.user.login, 'text': new_comment.text, 'created_at': new_comment.created_at.
            strftime('%-d %b %Y %H:%M'), 'to_comment_id': new_comment.to_comment_id,
                    'comment_id': new_comment.comment_id}]
        return JsonResponse(comment, safe=False)


class MovieCommentsView(DetailView):
    model = Movie
    template_name = 'comments.html'

    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(movie_id=kwargs['pk'])
        paginator = Paginator(Comment.objects.filter(movies=movie).order_by('created_at'), 10)
        comments = paginator.page(1)
        if request.is_ajax():
            page = int(request.GET.get('next_page'))
            if paginator.page(page).has_next:
                try:
                    comments = paginator.page(page)
                except PageNotAnInteger:
                    comments = paginator.page(1)
                except EmptyPage:
                    comments = paginator.page(paginator.num_pages)
                comments_page = list(map(lambda comment: comment.as_dict(), list(comments)))
                return JsonResponse({'comments_page': comments_page}, safe=False)
        return render(request, 'comments.html', context={'comments': comments, 'movie': movie})


class SelectionListView(ListView):
    model = Selection
    template_name = 'selections.html'


class SelectionDetailView(DetailView):
    model = Selection
    template_name = 'selection_detail.html'


class FavoritesCreateView(View):
    model = Bookmark

    def post(self, *args, **kwargs):
        movie_id = self.request.POST.get('movie_id')
        user_pk = self.request.POST.get('user_pk')
        user = OCUser.objects.get(pk=user_pk)
        movie = Movie.objects.get(movie_id=movie_id)
        bookmark = Bookmark.objects.create(user=user, movie=movie)
        response_bookmark = [{'user': bookmark.user.login, 'movie': bookmark.movie.name}]
        return JsonResponse(response_bookmark, safe=False)


class FavoritesDeleteView(DeleteView):
    model = Bookmark

    def delete(self, *args, **kwargs):
        movie_id = self.request.POST.get('movie_id')
        user_pk = self.request.POST.get('user_pk')
        user = OCUser.objects.get(pk=user_pk)
        movie = Movie.objects.get(movie_id=movie_id)
        bookmark = Bookmark.objects.filter(user=user, movie=movie)
        bookmark[0].delete()
        old_bookmark = [{'movie': movie.name}]
        return JsonResponse(old_bookmark, safe=False)



