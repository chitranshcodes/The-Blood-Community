from django.urls import path
from . import views

app_name='community'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('needblood/', views.NeedBlood.as_view(), name='needblood'),
    path('about/', views.About.as_view(), name='about'),
    path('donateblood/', views.DonateBlood.as_view(), name='donateblood'),
    path('communityandposts/', views.CommunityAndPosts.as_view(), name='communityandposts'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('requestblood/', views.RequestBlood.as_view(), name='requestblood')
]
