import random
from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser

from django_seed import Seed

from users.models import User
from categories.models import Category

NAME = "users"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--total", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        total = options.get("total", 1)
        categories = Category.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            total,
            {
                "fav_book_category": lambda x: random.choice(categories),
                "fav_movie_category": lambda x: random.choice(categories),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Create {total} {NAME}"))
