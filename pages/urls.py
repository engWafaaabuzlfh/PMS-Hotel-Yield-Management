from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginView, name="LoginForm"),
    path('sign-up',views.signupView, name="SignUPForm"),
    path('',views.mainView, name="MainForm"),
    path('reversation',views.reverseView, name="ReverseForm"),


]