from django.views.generic import ListView
from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator

from categories.models import Category
from books.models import Book
from movies.models import Movie


class GenreListView(ListView):

    """Genre List View"""

    model = Category
    template_name = "pages/genres/genre_list.html"
    context_object_name = "genres"
    paginate_by = 12
    paginate_orphans = 6
    ordering = "created"

    def get_context_data(self):
        page = int(self.request.GET.get("page", 1))
        page_sector = (page - 1) // 5
        page_sector = page_sector * 5
        context = super().get_context_data()
        context["page_sector"] = page_sector
        return context


def bookAndMovieByCategoryView(request, pk):

    """Book and Movie by Category View Definition"""

    print(pk)

    categories = Category.objects.all().order_by("pk")

    category = Category.objects.get(pk=pk)
    category_name = category.name
    books = Book.objects.filter(category=category)
    movies = Movie.objects.filter(categories=category)

    book_paginator = Paginator(books, 10, orphans=5)
    movie_paginator = Paginator(movies, 10, orphans=5)

    page = int(request.GET.get("page", 1))

    try:
        books = book_paginator.get_page(int(page))
    except EmptyPage:
        books = None

    try:
        movies = movie_paginator.get_page(int(page))
    except EmptyPage:
        movies = None

    book_count = books.paginator.num_pages
    movie_count = movies.paginator.num_pages

    if book_count > movie_count:
        max_page_obj = books
    else:
        max_page_obj = movies

    if page > max_page_obj.paginator.num_pages:
        page = max_page_obj.paginator.num_pages

    page_sector = (page - 1) // 5
    page_sector = page_sector * 5

    return render(
        request,
        "pages/category/movie_and_book_by_category.html",
        context={
            "categories": categories,
            "books": books,
            "movies": movies,
            "page_sector": page_sector,
            "max_page_obj": max_page_obj,
            "category_name": category_name,
        },
    )
