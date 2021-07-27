from django.views.generic import ListView, DetailView
from movies.models import Movie


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
