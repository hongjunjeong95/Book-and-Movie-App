from django.urls import path
from movies import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", movie_views.MovieDetailView.as_view(), name="movie-detail"),
    path("create/", movie_views.CreateMovieView.as_view(), name="movie-create"),
    path("<int:pk>/edit/", movie_views.EditMovieView.as_view(), name="movie-edit"),
]
