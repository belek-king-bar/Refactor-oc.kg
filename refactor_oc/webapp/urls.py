from django.urls import path

from webapp.views import MovieDetailView, BestsellerListView, FavoritesListView, ActorDetailView, MovieView, CatalogueListView, SearchListView, AjaxSearchView
from webapp.views import MovieDetailView, BestsellerListView, FavoritesListView, ActorDetailView, MovieView, \
    CatalogueListView, CommentCreateView

app_name = 'webapp'

urlpatterns = [
    path('', BestsellerListView.as_view(), name='bestseller_list'),
    path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('catalogue', CatalogueListView.as_view(), name='catalogue_list'),
    path('view/<int:pk>', MovieView.as_view(), name='view_movie'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail'),
    path('search/list', SearchListView.as_view(), name='search_list'),
    path('search/', AjaxSearchView.as_view(), name='search_view'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment')
]