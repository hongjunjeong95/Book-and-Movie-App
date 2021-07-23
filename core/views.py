from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book
from movies.models import Movie
from people.models import Person


def homeView(request):

    """Home View Definition"""

    books = Book.objects.all()
    movies = Movie.objects.all()
    people = Person.objects.all()

    book_paginator = Paginator(books, 10)
    movie_paginator = Paginator(movies, 10)
    person_paginator = Paginator(people, 10)

    book_page_number = request.GET.get("books_page", 1)
    movie_page_number = request.GET.get("movies_page", 1)
    people_page_number = request.GET.get("people_page", 1)
    print(people_page_number)

    book_page_obj = book_paginator.get_page(book_page_number)
    movie_page_obj = movie_paginator.get_page(movie_page_number)
    person_page_obj = person_paginator.get_page(people_page_number)

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
