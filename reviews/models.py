from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    text = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_by = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        "movies.Movie",
        related_name="reviews",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        "books.Book",
        related_name="reviews",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text
