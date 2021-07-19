from django.core.management.base import BaseCommand
from django_seed import Seed
from people import models as people_models

NAME = "people"


class Command(BaseCommand):
    help = f"This command creates many {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args, **options):
        total = options.get("total", 1)
        seeder = Seed.seeder()
        seeder.add_entity(
            people_models.Person,
            total,
            {
                "name": lambda x: seeder.faker.name(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"Successfully create {total} {NAME}"))
