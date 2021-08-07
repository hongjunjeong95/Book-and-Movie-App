from reviews.models import Review
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.http import Http404

from reviews.forms import CreateReviewForm
from books.models import Book
from movies.models import Movie
from users.mixins import LoggedInOnlyView


class CreateReviewView(LoggedInOnlyView, CreateView):
    form_class = CreateReviewForm
    template_name = "pages/reviews/create_review.html"

    def form_valid(self, form):
        review = form.save()
        review.created_by = self.request.user

        type = self.request.GET.get("type")
        id = self.request.GET.get("id")

        if type == "book":
            book = Book.objects.get(pk=id)
            review.book = book
            review.save()
            return redirect(reverse("books:book-detail", kwargs={"pk": id}))
        elif type == "movie":
            movie = Movie.objects.get(pk=id)
            review.movie = movie
            review.save()
            return redirect(reverse("movies:movie-detail", kwargs={"pk": id}))

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def deleteReview(request):
    reviewId = request.GET.get("reviewId")
    type = request.GET.get("type")
    review = Review.objects.get(pk=reviewId)

    if type == "book":
        contentPk = review.book.pk
    elif type == "movie":
        contentPk = review.movie.pk

    if review.created_by.pk != request.user.pk:
        raise Http404("Page not found")

    review.delete()

    return redirect(reverse(f"{type}s:{type}-detail", kwargs={"pk": contentPk}))
