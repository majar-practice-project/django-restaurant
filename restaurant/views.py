from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

def logout_view(request):
   logout(request)
   return redirect("index")