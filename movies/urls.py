from django.urls import path
from movies import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", movie_views.MovieDetailView.as_view(), name="movie-detail"),
]
