from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("signup_page",views.signup_page,name="signup_page"),
    path("login_page",views.login_page,name="login_page"),
    path("about_page",views.about_page,name="about_page"),

    
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout")
    
]
