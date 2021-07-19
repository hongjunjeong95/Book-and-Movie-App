import random
from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from django.db.models.query_utils import Q
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person

NAME = "books"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--total", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        total = options.get("total", 1)
        categories = Category.objects.all().filter(Q(kind="both") | Q(kind="book"))
        writers = Person.objects.all().filter(kind="writer")
        seeder = Seed.seeder()
        seeder.add_entity(
            Book,
            total,
            {
                "year": lambda x: random.randint(1900, 2021),
                "rating": lambda x: random.randint(0, 5),
                "category": lambda x: random.choice(categories),
                "writer": lambda x: random.choice(writers),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"Create {NAME}"))
