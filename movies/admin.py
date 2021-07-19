from django.contrib import admin

from movies import models as movie_models
from core.admin import RatingFilter


@admin.register(movie_models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """Movie Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "title",
                    "year",
                    "cover_image",
                    "rating",
                    "director",
                    "categories",
                    "casts",
                ),
            },
        ),
    )

    raw_id_fields = ("director",)

    filter_horizontal = (
        "categories",
        "casts",
    )

    list_display = (
        "title",
        "year",
        "cover_image",
        "rating",
        "director",
        "count_categories",
        "count_casts",
    )

    list_filter = (
        "year",
        RatingFilter,
        "director",
    )

    def count_categories(self, obj):
        return obj.categories.count()

    def count_casts(self, obj):
        return obj.casts.count()
