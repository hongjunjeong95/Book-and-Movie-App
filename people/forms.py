from django import forms
from people.models import Person


class CreatePersonForm(forms.ModelForm):

    """Create Person Form Definition"""

    class Meta:
        model = Person
        fields = (
            "name",
            "kind",
            "photo",
        )

    def save(self, *args, **kwargs):
        Movie = super().save(commit=False)
        return Movie
