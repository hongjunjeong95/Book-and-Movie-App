from django import forms
from books.models import Book


class CreateBookForm(forms.ModelForm):

    """Create Book Form Definition"""

    class Meta:
        model = Book
        fields = (
            "title",
            "year",
            "rating",
            "category",
            "writer",
            "cover_image",
        )

    def save(self, *args, **kwargs):
        book = super().save(commit=False)
        return book
