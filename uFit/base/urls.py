from django.urls import path
from . import views


urlpatterns = [path("", views.say_hello, name="hello"),
               path("privacy/", views.privacyPage, name="privacy"),
               path("home/", views.homePage, name="home"),]
