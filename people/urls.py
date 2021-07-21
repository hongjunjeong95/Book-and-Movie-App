from django.urls import path
from people import views as person_views

app_name = "people"

urlpatterns = [
    path(
        "",
        person_views.PersonListView.as_view(),
        name="people",
    )
]
