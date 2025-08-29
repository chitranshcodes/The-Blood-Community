from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm, LoginForm, BRequestForm
from .models import Profile, BRequest


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    
class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    
class Login(View):
    def get(self, request):
        return render(request, 'login.html')