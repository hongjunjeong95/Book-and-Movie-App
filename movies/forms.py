from django import forms
from movies.models import Movie


class CreateMovieForm(forms.ModelForm):

    """Create Movie Form Definition"""

    class Meta:
        model = Movie
        fields = (
            "title",
            "year",
            "rating",
            "cover_image",
            "director",
            "categories",
            "casts",
        )

    def save(self, *args, **kwargs):
        Movie = super().save(commit=False)
        return Movie
