from django.shortcuts import render
from django.views.generic import DetailView
from webapp.models import Person

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Movies #TODO нужны модели

    def get(self, request, *args, **kwargs):
        context = {
            'pk': '1',
            'name': 'Name',
            'description': 'Description',
            'year': 'Year',
            'genres': ['genre1', 'genre2', 'genre3']

        }
        return render(request, 'movie_detail.html', context)


class ActorDetailView(DetailView):
    model = Person
    template_name = 'actor.html'

def Favorites_view(request):
    movie = Movies.objects.all()
    return render(request, 'favorite_view.html', context={
        'movies':movie
    })