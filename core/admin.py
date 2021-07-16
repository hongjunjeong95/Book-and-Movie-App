from django.contrib import admin


class RatingFilter(admin.SimpleListFilter):
    title = "rating"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return (
            ("5", "5"),
            ("4", "4"),
            ("3", "3"),
            ("2", "2"),
            ("1", "1"),
        )

    def queryset(self, request, queryset):
        if self.value() == "5":
            return queryset.filter(rating__lte=5)
        if self.value() == "4":
            return queryset.filter(rating__lte=4)
        if self.value() == "3":
            return queryset.filter(rating__lte=3)
        if self.value() == "2":
            return queryset.filter(rating__lte=2)
        if self.value() == "1":
            return queryset.filter(rating__lte=1)
