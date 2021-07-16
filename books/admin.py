from django.contrib import admin

from books import models as book_models
from core.admin import RatingFilter


@admin.register(book_models.Book)
class BookAdmin(admin.ModelAdmin):

    """Book Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "title",
                    "year",
                    "cover_image",
                    "rating",
                    "category",
                    "writer",
                ),
            },
        ),
    )

    list_display = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    )

    list_filter = (
        "year",
        RatingFilter,
        "category",
        "writer",
    )
