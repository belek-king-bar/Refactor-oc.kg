from django.urls import path
from webapp.views import MovieDetailView, ActorDetailView, FavoritesListView

app_name = 'webapp'

urlpatterns = [
    path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail'),

]