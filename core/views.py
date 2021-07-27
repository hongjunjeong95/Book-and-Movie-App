from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from books.models import Book
from movies.models import Movie
from people.models import Person


def homeView(request):

    """Home View Definition"""

    books = Book.objects.all().order_by("-pk")
    movies = Movie.objects.all().order_by("pk")
    people = Person.objects.all().order_by("pk")

    book_paginator = Paginator(books, 10, orphans=5)
    movie_paginator = Paginator(movies, 10, orphans=5)
    person_paginator = Paginator(people, 10, orphans=5)

    page = int(request.GET.get("page", 1))

    try:
        books = book_paginator.get_page(int(page))
    except EmptyPage:
        books = None

    try:
        movies = movie_paginator.get_page(int(page))
    except EmptyPage:
        movies = None

    try:
        people = person_paginator.get_page(int(page))
    except EmptyPage:
        people = None

    print(books, movies, people)
    book_count = books.paginator.num_pages
    movie_count = movies.paginator.num_pages
    people_count = people.paginator.num_pages

    if book_count > movie_count:
        max_page_obj = books
    else:
        max_page_obj = movies

    if max_page_obj.paginator.num_pages < people_count:
        max_page_obj = people

    if page > max_page_obj.paginator.num_pages:
        page = max_page_obj.paginator.num_pages

    page_sector = (page - 1) // 5
    page_sector = page_sector * 5
    return render(
        request,
        "pages/root/home.html",
        {
            "books": books,
            "movies": movies,
            "people": people,
            "page_sector": page_sector,
            "max_page_obj": max_page_obj,
        },
    )


def searchView(request):
    return render(request, "pages/root/search.html")
