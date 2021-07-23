from django.urls import path
from books import views as book_views

app_name = "books"

urlpatterns = [
    path("", book_views.BookListView.as_view(), name="book-list"),
]
