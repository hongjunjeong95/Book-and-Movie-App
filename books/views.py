from django.views.generic import ListView
from books.models import Book


class BookListView(ListView):

    """Book List View"""

    model = Book
    template_name = "pages/books/book_list.html"
    context_object_name = "books"
    paginate_by = 10
    paginate_orphans = 5
    ordering = ["-year"]

    def get_context_data(self):
        page = int(self.request.GET.get("page", 1))
        page_sector = (page - 1) // 5
        page_sector = page_sector * 5
        context = super().get_context_data()
        context["page_sector"] = page_sector
        return context
