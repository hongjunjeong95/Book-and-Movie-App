from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.shortcuts import redirect, reverse

from movies.models import Movie
from movies.forms import CreateMovieForm


class MovieListView(ListView):

    """Movie List View"""

    model = Movie
    template_name = "pages/movies/movie_list.html"
    context_object_name = "movies"
    paginate_by = 10
    paginate_orphans = 6
    ordering = "created"

    def get_context_data(self):
        page = int(self.request.GET.get("page", 1))
        page_sector = (page - 1) // 5
        page_sector = page_sector * 5
        context = super().get_context_data()
        context["page_sector"] = page_sector
        return context


class MovieDetailView(DetailView):

    """Movie Detail View"""

    model = Movie
    template_name = "pages/movies/movie_detail.html"


class CreateRoomView(FormView):

    """Create Movie View Definition"""

    form_class = CreateMovieForm
    template_name = "pages/movies/create_movie.html"

    def form_valid(self, form):
        movie = form.save()
        movie.save()
        form.save_m2m()
        return redirect(reverse("movies:movie-detail", kwargs={"pk": movie.pk}))


class EditMovieView(UpdateView):

    """Edit Movie View Definition"""

    model = Movie
    template_name = "pages/movies/edit_movie.html"
    fields = (
        "title",
        "year",
        "rating",
        "director",
        "categories",
        "casts",
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
