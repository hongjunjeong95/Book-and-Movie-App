import random
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser
from django.db.models.query_utils import Q
from django.contrib.admin.utils import flatten

from django_seed import Seed

from movies.models import Movie
from categories.models import Category
from people.models import Person

NAME = "movies"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--total", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        total = options.get("total", 1)
        directors = Person.objects.all().filter(kind="director")
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie,
            total,
            {
                "year": lambda x: random.randint(1900, 2021),
                "rating": lambda x: random.randint(0, 5),
                "director": lambda x: random.choice(directors),
                "cover_image": lambda x: f"movie_cover_images/{random.randint(1,10)}.jpg",
            },
        )
        created_movies = seeder.execute()
        movie_pks = flatten(created_movies.values())

        categories = Category.objects.all().filter(Q(kind="both") | Q(kind="movie"))
        casts = Person.objects.all().filter(kind="actor")

        for movie_pk in movie_pks:
            movie = Movie.objects.get(pk=movie_pk)
            for category in categories:
                magic_number = random.randint(0, 21)
                if magic_number % 2 == 0:
                    movie.categories.add(category)

            for cast in casts:
                magic_number = random.randint(0, 16)
                if magic_number % 2 == 0:
                    movie.casts.add(cast)

        self.stdout.write(self.style.SUCCESS(f"Create {total} {NAME}"))
