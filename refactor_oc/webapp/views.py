from django.shortcuts import render
from django.views.generic import DetailView
from webapp.models import Person, Movie, Rating, Participant, Genre
from django.views.generic import DetailView, ListView
from webapp.models import Bestseller, Movie, Person, Bookmark
import json


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['oc_kg'] = Rating.objects.get(movie=self.object, system='local')
        context['imdb'] = Rating.objects.get(movie=self.object, system='imdb')
        context['kinopoisk'] = Rating.objects.get(movie=self.object, system='kinopoisk')
        context['producers'] = Participant.objects.filter(movie=self.object, role_id=1)
        context['actors'] = Participant.objects.filter(movie=self.object, role_id=3)
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
            return Movie.objects.filter(genres__in=res[:3])[:5]
        else:
            return Movie.objects.filter(genres__in=res)[:5]






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

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
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
