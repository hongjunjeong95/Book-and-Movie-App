from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.shortcuts import redirect, reverse

from books.models import Book
from books.forms import CreateBookForm


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


class BookDetailView(DetailView):

    """Book Detail View"""

    model = Book
    template_name = "pages/books/book_detail.html"


class CreateBookmView(FormView):

    """Create Book View Definition"""

    form_class = CreateBookForm
    template_name = "pages/books/create_book.html"

    def form_valid(self, form):
        book = form.save()
        book.save()
        return redirect(reverse("books:book-detail", kwargs={"pk": book.pk}))


class EditBookView(UpdateView):

    """Edit Book View Definition"""

    model = Book
    template_name = "pages/books/edit_book.html"
    fields = (
        "title",
        "year",
        "rating",
        "category",
        "writer",
    )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["title"].widget.attrs = {"class": "w-full", "placeholder": "Title"}
        form.fields["year"].widget.attrs = {"class": "w-full", "placeholder": "Year"}
        form.fields["rating"].widget.attrs = {
            "class": "w-full",
            "placeholder": "Rating",
        }
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
