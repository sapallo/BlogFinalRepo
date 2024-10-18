from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as LoginViewDjango
from django.contrib.auth.views import LogoutView as LogoutViewDjango
from apps.user.forms import RegisterForm, LoginForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy


class UserProfileView(TemplateView):
    template_name = 'user/user_profile.html'

class RegisterView(CreateView):
    template_name = 'auth/auth_register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        registered_group = Group.objects.get(name='Registered')
        self.object.groups.add(registered_group)

        return response
    
class LoginView(LoginViewDjango):
    template_name = 'auth/auth_login.html'
    authentication_form = LoginForm


    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('home')


class LogoutView(LogoutViewDjango):
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('home')
    