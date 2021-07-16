from django.db import models
from core import models as core_models


class FavList(core_models.TimeStampedModel):

    """Fav Model Definition"""

    created_by = models.OneToOneField(
        "users.User", related_name="favList", on_delete=models.CASCADE
    )

    books = models.ManyToManyField("books.Book", related_name="favLists", blank=True)
    movies = models.ManyToManyField("movies.Movie", related_name="favLists", blank=True)

    def __str__(self):
        return f"{self.created_by}'s Fav List"
