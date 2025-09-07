from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, LoginForm, BRequestForm, ProfileForm
from .models import Profile, BRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
import os
from django.conf import settings
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    
class Register(View):
    def get(self, request):
        form=RegistrationForm()
        return render(request, 'register.html', {'form':form})
    def post(self, request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            bgroup=form.cleaned_data['bgroup']
            district=form.cleaned_data['district']

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already registered')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                Profile.objects.create(district=district, bgroup=bgroup, user=user)
                messages.success(request, "Registered Successfully🤩 Login now!")
                return redirect('community:login')
        return render(request, 'register.html', {'form':form})


class Login(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'login.html', {'form':form})
    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            messages.success(request, "Logged-In Successfully🤩 Welcome back!")
            return redirect("community:home")
        else:
            form.add_error(None, "username or email doesn't match")
    
        return render(request, "login.html", {'form':form})
    
@method_decorator(login_required, name='dispatch')    
class NeedBlood(View):
    def get(self, request):
        current_user=request.user
        json_path=os.path.join(settings.BASE_DIR, 'community', "data", 'blood_bank.json')
        with open(json_path, "r", encoding='utf-8') as f:
            blood_banks=json.load(f)
        district=current_user.profile.district
        blood_bank=[]
        if district:
            blood_bank=[b for b in blood_banks if b["district"].lower()==district.lower()]

        return render(request, 'needblood.html', {"bloodbanks":blood_bank, "current_user":current_user})
    
@method_decorator(login_required, name='dispatch')    
class RequestBlood(View):
    def get(self, request):
        current_user=request.user
        form= BRequestForm(initial={
            'bgroup':current_user.profile.bgroup,
            'district':current_user.profile.district
        })
        return render(request, 'bloodrequest.html', {"form":form})
    def post(self, request):
        form=BRequestForm(request.POST)
        current_user=request.user
        if form.is_valid():
            district=form.cleaned_data['district']
            bgroup=form.cleaned_data['bgroup']
            BRequest.objects.create(district=district, bgroup=bgroup, user=current_user)
            messages.success(request, "Requirement Added for Donation Request")
            return redirect('community:donateblood')
        return render(request, 'bloodrequest.html', {"form":form})

class About(View):
    def get(self, request):
        return render(request, 'about.html')
    
class DonateBlood(View):
    def get(self, request):
        return render(request, 'donateblood.html')

class CommunityAndPosts(View):
    def get(self, request):
        return render(request, 'communityandposts.html')
    
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        current_user=request.user
        form= ProfileForm(initial={
        'bgroup':current_user.profile.bgroup,
        'district':current_user.profile.district})
        return render(request, 'profile.html', {'form': form , 'user':current_user})
    def post(self, request):
        current_user=request.user
        form=ProfileForm(request.POST)
        if form.is_valid():
            district=form.cleaned_data['district']
            bgroup=form.cleaned_data['bgroup']
            current_user.profile.district=district
            current_user.profile.bgroup=bgroup
            current_user.profile.save()
            messages.success(request, "Profile Updated successfully...")
            return redirect('community:home')
        return render(request, 'profile.html', {'form':form, 'user':current_user})

    
@login_required
def Logout(request):
    logout(request)
    messages.success(request, "Fir Milenge! Stay safe...")
    return redirect("community:home")