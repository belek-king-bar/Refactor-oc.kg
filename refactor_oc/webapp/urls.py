from django.urls import path
from webapp.views import MovieDetailView, ActorDetailView

app_name = 'webapp'

urlpatterns = [
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail')
]