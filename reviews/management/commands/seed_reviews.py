import random
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from django_seed import Seed

from reviews.models import Review
from users.models import User
from movies.models import Movie
from books.models import Book

NAME = "reviews"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--total", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        total = options.get("total", 1)
        users = User.objects.all()
        books = Book.objects.all()
        movies = Movie.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            total,
            {
                "text": lambda x: seeder.faker.sentence(),
                "rating": lambda x: random.randint(0, 5),
                "created_by": lambda x: random.choice(users),
                "movie": lambda x: random.choice(movies),
                "book": lambda x: random.choice(books),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Create {NAME}"))
