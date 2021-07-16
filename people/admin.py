from django.contrib import admin
from people import models as person_models


@admin.register(person_models.Person)
class PersonAdmin(admin.ModelAdmin):

    """Person Admin Definition"""

    fieldsets = (
        (
            "Baic Info",
            {
                "fields": (
                    "name",
                    "kind",
                    "photo",
                ),
            },
        ),
    )

    list_display = (
        "name",
        "kind",
        "photo",
    )

    list_filter = ("kind",)
