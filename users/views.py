from django.contrib.auth import authenticate
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.db.utils import IntegrityError

from users.forms import SignUpForm


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
