from django.views.generic import ListView
from people.models import Person


class PersonListView(ListView):

    """Person List View"""

    model = Person
    template_name = "pages/people/person_list.html"
    context_object_name = "people"
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
