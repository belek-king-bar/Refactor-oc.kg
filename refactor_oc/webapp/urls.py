from django.urls import path
from webapp.views import MovieDetailView, BestsellerListView, FavoritesListView, ActorDetailView, CatalogueListView

app_name = 'webapp'

urlpatterns = [
    path('', BestsellerListView.as_view(), name='bestseller_list'),
    path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail'),
    path('catalogue', CatalogueListView.as_view(), name='catalogue_list'),
]