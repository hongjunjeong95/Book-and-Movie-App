from django.urls import path
from favs import views as fav_views

app_name = "favs"

urlpatterns = [
    path("list/", fav_views.fav_list, name="favs-list"),
    # path("add/<int:pk>/", fav_views.FavsList.as_view(), name="add-fav"),
]
