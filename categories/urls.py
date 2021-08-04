from django.urls import path
from categories import views as category_views

app_name = "categories"

urlpatterns = [
    path("<int:pk>/", category_views.bookAndMovieByCategoryView, name="bookAndMovieByCategory"),
]
