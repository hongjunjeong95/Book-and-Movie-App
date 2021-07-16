from django.contrib import admin
from categories import models as category_models


@admin.register(category_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("name", "kind"),
            },
        ),
    )

    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
