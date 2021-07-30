from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
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

    def get_success_url(self):
        return self.request.user.get_absolute_url()


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


# @login_required
# def change_password(request, pk):
#     if request.method == "GET":
#         try:
#             if request.user.login_method != "email":
#                 raise EmailLoggedInOnly("Page not found 404")
#             if request.user.pk != pk:
#                 raise Http404("Page Not found 404")
#             user = models.User.objects.get_or_none(pk=pk)
#             if user is None:
#                 messages.error(request, "User does not exist")
#                 return redirect(reverse("core:home"))
#             return render(
#                 request,
#                 "pages/users/change_password.html",
#                 context={"user": user},
#             )
#         except EmailLoggedInOnly as error:
#             messages.error(request, error)
#             return redirect("core:home")
#     elif request.method == "POST":
#         try:
#             if request.user.login_method != "email":
#                 raise EmailLoggedInOnly("Page not found 404")
#             if request.user.pk != pk:
#                 raise Http404("Page Not found 404")
#             user = models.User.objects.get_or_none(pk=pk)
#             if user is None:
#                 messages.error(request, "User does not exist")
#                 return redirect(reverse("core:home"))
#             old_password = request.POST.get("current_password")
#             new_password = request.POST.get("new_password")
#             new_password1 = request.POST.get("verify_password")
#             user = authenticate(request, username=user.email, password=old_password)
#             if user is None:
#                 raise ChangePasswordException("Current password is wrong!")

#             if new_password != new_password1:
#                 raise ChangePasswordException("New password doesn't match")
#             user.set_password(new_password)
#             user.save()
#             messages.success(request, f"{user.email}'password changed successfully")
#             login(request, user)
#             return redirect(reverse("users:profile", kwargs={"pk": pk}))
#         except ChangePasswordException as error:
#             messages.error(request, error)
#             return redirect(reverse("core:home"))
#         except EmailLoggedInOnly as error:
#             messages.error(request, error)
#             return redirect("core:home")


class ChangePasswordView(PasswordChangeView):
    template_name = "pages/users/change_password.html"
    success_message = "Password changed"

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].widget.attrs = {"placeholder": "Old password"}
        form.error_messages["password_mismatch"] = "The two password didn't match"
        form.fields["new_password1"].widget.attrs = {"placeholder": "New password"}
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "Verify your new password"
        }
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()
