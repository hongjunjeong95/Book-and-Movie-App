from django.urls import path
from reviews import views as review_views

app_name = "reviews"

urlpatterns = [
    path("create/", review_views.CreateReviewView.as_view(), name="create-review"),
]
