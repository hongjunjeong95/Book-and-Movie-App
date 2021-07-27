from django.urls import path
from people import views as person_views

app_name = "people"

urlpatterns = [
    path(
        "",
        person_views.PersonListView.as_view(),
        name="person-list",
    ),
    path(
        "<int:pk>/",
        person_views.PeopleDetailView.as_view(),
        name="person-detail",
    ),
    path(
        "create/",
        person_views.CreatePersonView.as_view(),
        name="person-create",
    ),
    path(
        "<int:pk>/edit/",
        person_views.EditPersonView.as_view(),
        name="person-edit",
    ),
]
