from django.urls import path
from webapp.views import MovieDetailView

app_name = 'webapp'

urlpatterns = [
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
]