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

    list_display = ("created_by",)

    list_filter = ("created_by",)
