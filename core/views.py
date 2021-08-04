from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from books.models import Book
from movies.models import Movie
from people.models import Person
from categories.models import Category


def homeView(request):

    """Home View Definition"""

    categories = Category.objects.all().order_by("pk")
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
            "categories": categories,
        },
    )


def searchView(request):

    """Search View Definition"""

    categories = Category.objects.all().order_by("pk")

    searchgin_term = request.GET.get("name", None)

    people: Person.objects = None

    books = Book.objects.filter(title__contains=searchgin_term)
    movies = Movie.objects.filter(title__contains=searchgin_term)
    people = Person.objects.filter(name__contains=searchgin_term)

    book_paginator = Paginator(books, 10, orphans=5)
    movie_paginator = Paginator(movies, 10, orphans=5)

    page = int(request.GET.get("page", 1))
    people_count = 0

    person_paginator = Paginator(people, 10, orphans=5)
    try:
        people = person_paginator.get_page(int(page))
    except EmptyPage:
        people = None
    people_count = people.paginator.num_pages

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

    #
    if max_page_obj.paginator.num_pages < people_count:
        max_page_obj = people

    if page > max_page_obj.paginator.num_pages:
        page = max_page_obj.paginator.num_pages

    page_sector = (page - 1) // 5
    page_sector = page_sector * 5

    return render(
        request,
        "pages/root/search.html",
        context={
            "categories": categories,
            "books": books,
            "movies": movies,
            "people": people,
            "page_sector": page_sector,
            "max_page_obj": max_page_obj,
            "searchgin_term": searchgin_term,
        },
    )
