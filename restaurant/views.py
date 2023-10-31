from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

class Login(LoginView):
   redirect_authenticated_user = True

   def get_success_url(self):
    if self.request.user.is_authenticated:
        # Redirect logged-in users to the home page.
        return reverse('index')
    else:
        return reverse('login')

def logout_view(request):
   logout(request)
   return redirect("index")