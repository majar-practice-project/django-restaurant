from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponseBadRequest('Wrong credentials')
    return HttpResponseBadRequest('Bad request')


def logout_view(request):
   logout(request)
   return redirect("index")