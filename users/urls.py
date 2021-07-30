from django.urls import path
from users import views as user_views

app_name = "users"

urlpatterns = [
    path("signup/", user_views.SignUpView.as_view(), name="signup"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", user_views.log_out, name="logout"),
    path("<int:pk>/profile/", user_views.UserProfileView.as_view(), name="profile"),
    path(
        "<int:pk>/update-profile/",
        user_views.UpdateProfileView.as_view(),
        name="update-profile",
    ),
    path(
        "<int:pk>/change-password/",
        user_views.ChangePasswordView.as_view(),
        name="change-password",
    ),
]
