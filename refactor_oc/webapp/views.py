from django.shortcuts import render
from django.views.generic import DetailView
from webapp.models import Person

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'

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
