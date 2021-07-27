from django.urls import path
from books import views as book_views

app_name = "books"

urlpatterns = [
    path("", book_views.BookListView.as_view(), name="book-list"),
    path("<int:pk>/", book_views.BookDetailView.as_view(), name="book-detail"),
]
