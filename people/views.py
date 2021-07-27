from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.shortcuts import redirect, reverse

from people.models import Person
from people.forms import CreatePersonForm


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


class PeopleDetailView(DetailView):

    """People Detail View"""

    model = Person
    template_name = "pages/people/person_detail.html"


class CreatePersonView(FormView):

    """Create Person View Definition"""

    form_class = CreatePersonForm
    template_name = "pages/people/create_person.html"

    def form_valid(self, form):
        person = form.save()
        person.save()
        return redirect(reverse("people:person-detail", kwargs={"pk": person.pk}))


class EditPersonView(UpdateView):

    """Edit Person View Definition"""

    model = Person
    template_name = "pages/people/edit_person.html"
    fields = (
        "name",
        "kind",
        "photo",
    )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].widget.attrs = {"class": "w-full", "placeholder": "Title"}
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
