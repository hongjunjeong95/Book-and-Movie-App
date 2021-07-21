from django.urls import path
from categories import views as genre_views

app_name = "genres"

urlpatterns = [
    path("", genre_views.GenreListView.as_view(), name="genres"),
]
