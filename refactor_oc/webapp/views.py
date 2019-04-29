from webapp.models import Person, Bookmark
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth

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


class FavoritesListView(ListView):
    model = Bookmark
    template_name = 'favorite_view.html'

    def post(self, request):
        if request.user.is_authenticated():
            return self.model.objects.get().order_by('-created_at')
        else:
            return
        pass #todo сделать редирект(?) на главную/логинку
