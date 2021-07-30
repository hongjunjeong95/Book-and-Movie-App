from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.db.utils import IntegrityError

from users.forms import LoginForm, SignUpForm
from users.models import User


class SignUpView(FormView):

    """Sign Up View"""

    form_class = SignUpForm
    success_url = reverse_lazy("core:home")
    template_name = "pages/users/signup.html"

    def form_valid(self, form):
        try:
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            authenticate(self.request, username=email, password=password)
            return super().form_valid(form)
        except IntegrityError:
            return redirect(reverse("users:signup"))


class LoginView(FormView):

    """Login View"""

    form_class = LoginForm
    success_url = reverse_lazy("core:home")
    template_name = "pages/users/login.html"

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return redirect(reverse("users:login"))
        return super().form_valid(form)


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class UserProfileView(DetailView):

    """User Profile View"""

    model = User
    context_object_name = "user_obj"
    template_name = "pages/users/user_profile.html"


class UpdateProfileView(UpdateView):

    """Update Profile View Definition"""

    model = User
    fields = {
        "first_name",
        "last_name",
        "email",
        "language",
        "preference",
        "fav_book_category",
        "fav_movie_category",
        "bio",
    }
    template_name = "pages/users/edit_profile.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["email"].widget.attrs = {"placeholder": "Email"}
        form.fields["first_name"].widget.attrs = {"placeholder": "First name"}
        form.fields["last_name"].widget.attrs = {"placeholder": "Last name"}
        form.fields["bio"].widget.attrs = {
            "placeholder": "Bio",
            "class": "resize-none w-full",
            "rows": "10",
        }
        return form


# class UpdateProfileView(FormView):

#     """Update Profile View Definition"""

#     form_class = UpdateProfileForm
#     success_url = reverse_lazy("users:home")

#     template_name = "pages/users/edit_profile.html"
#     success_message = "Profile Updated"

#     # def get_form(self, form_class=None):
#     #     form = super().get_form(form_class=form_class)
#     #     form.fields["email"].widget.attrs = {"placeholder": "Email"}
#     #     form.fields["first_name"].widget.attrs = {"placeholder": "First name"}
#     #     form.fields["last_name"].widget.attrs = {"placeholder": "Last name"}
#     #     form.fields["bio"].widget.attrs = {"placeholder": "Bio"}
#     #     return form

#     def form_valid(self, form):
#         user = form.save()
#         user.save()
#         print(user)
#         return redirect(reverse("users:user-profile", kwargs={"pk": user.pk}))
