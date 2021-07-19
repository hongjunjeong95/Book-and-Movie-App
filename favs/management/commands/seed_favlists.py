import random
from typing import Any, Optional

from django.core.management.base import BaseCommand

from favs.models import FavList
from users.models import User
from books.models import Book
from movies.models import Movie

NAME = "favourite lists"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    # def add_arguments(self, parser: CommandParser) -> None:
    #     parser.add_argument(
    #         "--total", type=int, help=f"How many {NAME} do you want to create"
    #     )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users = User.objects.all()

        books = Book.objects.all()
        movies = Movie.objects.all()

        for user in users:
            favList = FavList.objects.create(created_by=user)

            for book in books:
                magic_number = random.randint(0, 50)
                if magic_number % 2 == 0:
                    favList.books.add(book)
            for movie in movies:
                magic_number = random.randint(0, 50)
                if magic_number % 2 == 0:
                    favList.movies.add(movie)

        self.stdout.write(self.style.SUCCESS(f"Create {NAME}"))
