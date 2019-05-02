from django.urls import path
from webapp.views import MovieDetailView, BestsellerListView, FavoritesListView, ActorDetailView, MovieView

app_name = 'webapp'

urlpatterns = [
    path('', BestsellerListView.as_view(), name='bestseller_list'),
    path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('view/<int:pk>', MovieView.as_view(), name='view_movie'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail')
]