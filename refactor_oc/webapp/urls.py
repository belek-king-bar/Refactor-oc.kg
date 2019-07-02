from django.urls import path


from webapp.views import MovieDetailView, BestsellerListView, CommentCreateView, FavoritesListView, \
    ActorDetailView, MovieView, CatalogueListView, SelectionListView, SelectionDetailView, \
    SearchListView, AjaxSearchView, FavoritesCreateView, FavoritesDeleteView, MovieCommentsView, CommentAnswerView



app_name = 'webapp'

urlpatterns = [
    path('', BestsellerListView.as_view(), name='bestseller_list'),
    path('favorites/', FavoritesListView.as_view(), name='favorites_list'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('catalogue', CatalogueListView.as_view(), name='catalogue_list'),
    path('selections/', SelectionListView.as_view(), name='selection_list'),
    path('selections/<int:pk>', SelectionDetailView.as_view(), name='selection_detail'),
    path('view/<int:pk>', MovieView.as_view(), name='view_movie'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail'),
    path('search/list', SearchListView.as_view(), name='search_list'),
    path('search/', AjaxSearchView.as_view(), name='search_view'),
    path('add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('answer_comment/', CommentAnswerView.as_view(), name='answer_comment'),
    path('movie/<int:pk>/comments', MovieCommentsView.as_view(), name='movie_comments'),
    path('to_favorites/', FavoritesCreateView.as_view(), name='to_favorites'),
    path('from_favorites/', FavoritesDeleteView.as_view(), name='from_favorites')
]