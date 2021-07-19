import random
from django.core.management.base import BaseCommand
from categories.models import Category

NAME = "categories"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def handle(self, *args, **options):
        categories = [
            "Action",
            "Comedy",
            "Drama",
            "Western",
            "Fantasy",
            "Adventure",
            "Romance",
            "Contemporary",
            "Dystopian",
            "Mystery",
            "Horror",
            "Thriller",
            "Paranormal",
            "Historical fiction",
            "Science Fiction",
            "Memoir",
            "Cooking",
            "Art",
            "Self-help / Personal",
            "Development",
            "Motivational",
            "Health",
            "History",
            "Travel",
            "Guide / How-to",
            "Families & Relationships",
            "Humor",
            "Children’s",
        ]

        kind = [Category.KIND_BOOK, Category.KIND_MOVIE, Category.KIND_BOTH]

        for category in categories:
            Category.objects.create(name=category, kind=random.choice(kind))

        self.stdout.write(self.style.SUCCESS(f"Create {NAME}"))
