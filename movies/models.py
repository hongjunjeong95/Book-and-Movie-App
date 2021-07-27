from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
from django.shortcuts import reverse

from core import models as core_models


class Movie(core_models.TimeStampedModel):

    """Movie Model Definition"""

    title = models.CharField(max_length=20)
    year = models.IntegerField(validators=[MinValueValidator(0)])
    cover_image = models.ImageField(upload_to="movie_cover_images", blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    director = models.ForeignKey(
        "people.Person",
        related_name="moviesDirector",
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"kind": "director"},
    )
    categories = models.ManyToManyField(
        "categories.Category",
        related_name="movies",
        blank=True,
        limit_choices_to=Q(kind="both") | Q(kind="movie"),
    )
    casts = models.ManyToManyField(
        "people.Person",
        related_name="moviesCasts",
        blank=True,
        limit_choices_to={"kind": "actor"},
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie-detail", kwargs={"pk": self.pk})
