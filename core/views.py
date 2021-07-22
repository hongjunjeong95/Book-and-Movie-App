from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from books.models import Book
from movies.models import Movie
from people.models import Person


class HomeView(ListView):

    """Home View Definition"""

    model = Book
    template_name = "pages/root/home.html"
    context_object_name = "books"
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


def homeView(request):
    books = Book.objects.all()
    movies = Movie.objects.all()
    people = Person.objects.all()

    book_paginator = Paginator(books, 8)
    movie_paginator = Paginator(movies, 8)
    person_paginator = Paginator(people, 8)

    page_number = request.GET.get("page", 1)

    book_page_obj = book_paginator.get_page(page_number)
    movie_page_obj = movie_paginator.get_page(page_number)
    person_page_obj = person_paginator.get_page(page_number)

    return render(
        request,
        "pages/root/home.html",
        {
            "book_page_obj": book_page_obj,
            "movie_page_obj": movie_page_obj,
            "person_page_obj": person_page_obj,
        },
    )


def searchView(request):
    return render(request, "pages/root/search.html")
