from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView
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
