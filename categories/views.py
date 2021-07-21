from django.views.generic import ListView
from categories.models import Category as Genre


class GenreListView(ListView):

    """Genre List View"""

    model = Genre
    template_name = "pages/genres/genre_list.html"
    context_object_name = "genres"
    paginate_by = 12
    paginate_orphans = 6
    ordering = "created"

    def get_context_data(self):
        page = int(self.request.GET.get("page", 1))
        page_sector = (page - 1) // 5
        page_sector = page_sector * 5
        context = super().get_context_data()
        context["page_sector"] = page_sector
        return context
