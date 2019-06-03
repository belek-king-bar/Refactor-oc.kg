from webapp.models import Rating, Participant
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView, ListView, View
from webapp.models import Bestseller, Movie, Person, Bookmark, Comment, Genre, Selection, OCUser
from django.views.generic.base import TemplateView
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.template import loader

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

    def post(self, request):
        if request.user.is_authenticated():
            return self.model.objects.get().order_by('-created_at')
        else:
            return
        pass #todo сделать редирект(?) на главную/логинку


class BestsellerListView(ListView):
    model = Bestseller
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['paginator'] = Paginator(all_movies, 4)
        context['page'] = self.request.GET.get('page')
        context['movies'] = context['paginator'].get_page(context['page'])
        return context


class MovieView(DetailView):
    model = Movie
    template_name = 'view_movie.html'

    def get_context_data(self, **kwargs):
        context = super(MovieView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(movies=self.object).order_by('-created_at')[:10]
        context['comments_len'] = len(Comment.objects.filter(movies=self.object))
        if self.object.group:
            context['compilation'] = Movie.objects.filter(group=self.object.group)
        else:
            context['compilation'] = self.get_compilation_by_genres(Genre.objects.filter(movies__in=[self.object.movie_id]))
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
        user = OCUser.objects.get(pk=user_pk)
        movie = Movie.objects.get(movie_id=movie_id)
        new_comment = movie.comments.create(user=user, text=text)
        comment = [{'user': new_comment.user.login, 'text': new_comment.text, 'created_at': new_comment.created_at.
             strftime('%-d %B %Y %H:%M')}]
        return JsonResponse(comment, safe=False)

class MovieCommentsView(DetailView):
    model = Movie
    template_name = 'comments.html'

    # def get_context_data(self, **kwargs):
    #     context = super(MovieCommentsView, self).get_context_data(**kwargs)
    #     paginator = Paginator(Comment.objects.filter(movies=self.object).order_by('created_at'), 10)
    #     context['comments'] = paginator.page(1)
    #     return context


    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(movie_id=kwargs['pk'])
        # comments = Comment.objects.all().order_by('created_at')[:20]
        paginator = Paginator(Comment.objects.filter(movies=movie).order_by('created_at'), 10)
        comments = paginator.page(1)
        template = loader.get_template('comments.html')
        if request.is_ajax():
            page = request.GET.get('page', 1)
            print(page)
            paginator = Paginator(comments, 10)
            try:
                comments = paginator.page(page)
            except PageNotAnInteger:
                comments = paginator.page(1)
            except EmptyPage:
                comments = paginator.page(paginator.num_pages)
            comments_page = list(map(lambda comment: comment.as_dict(), list(comments)))
            print(comments_page)
            return JsonResponse(comments_page, safe=False)
        # return render_to_response('comments.html', {'comments': comments})
        # return HttpResponse(template.render({'comments': comments}))
        return render(request, 'comments.html', context={'comments': comments, 'movie': movie})


class SelectionListView(ListView):
    model = Selection
    template_name = 'selections.html'
