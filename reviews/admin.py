from core.admin import RatingFilter
from django.contrib import admin
from reviews import models as review_models


@admin.register(review_models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "text",
                    "rating",
                    "created_by",
                    "movie",
                    "book",
                ),
            },
        ),
    )

    list_display = (
        "text",
        "rating",
        "created_by",
        "movie",
        "book",
    )

    list_filter = (
        RatingFilter,
        "created_by",
        "movie",
        "book",
    )
