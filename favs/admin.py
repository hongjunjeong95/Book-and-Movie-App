from django.contrib import admin
from favs import models as fav_models


@admin.register(fav_models.FavList)
class FavListAdmin(admin.ModelAdmin):

    """Fav Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("created_by", "books", "movies"),
            },
        ),
    )

    filter_horizontal = (
        "books",
        "movies",
    )

    list_display = (
        "created_by",
        "count_books",
        "count_movies",
    )

    search_fields = ("created_by__username",)

    list_filter = ("created_by",)

    def count_books(self, obj):
        return obj.books.count()

    def count_movies(self, obj):
        return obj.movies.count()
