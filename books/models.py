from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

from core import models as core_models


class Book(core_models.TimeStampedModel):

    """Book Model Definition"""

    title = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(0)])
    cover_image = models.ImageField(upload_to="book_cover_images", blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    category = models.ForeignKey(
        "categories.Category",
        related_name="books",
        on_delete=models.CASCADE,
        null=True,
        limit_choices_to=Q(kind="both") | Q(kind="book"),
    )
    writer = models.ForeignKey(
        "people.Person",
        related_name="books",
        on_delete=models.CASCADE,
        limit_choices_to={"kind": "writer"},
    )

    def __str__(self):
        return self.title
