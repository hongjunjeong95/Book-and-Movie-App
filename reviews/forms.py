from django import forms

from reviews.models import Review


class CreateReviewForm(forms.ModelForm):

    """Create Review Form Definition"""

    class Meta:
        model = Review
        fields = {
            "text",
            "rating",
        }
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "w-full resize-none outline-none",
                    "placeholder": "Text",
                    "rows": "10",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "class": "w-full outline-none",
                    "placeholder": "Rating",
                    "min": 0,
                }
            ),
        }

    def save(self, *args, **kwargs):
        review = super().save(commit=False)
        return review
