from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book


class HomeView(ListView):

    """Home View Definition"""

    model = Book
    template_name = "pages/root/home.html"
    context_object_name = "books"
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


def searchView(request):
    return render(request, "pages/root/search.html")
