from django.urls import path
from . import views

# URLConf (URL Configuration)
urlpatterns = [
  # Routes should always end with forward slash.
  path('hello/', views.say_hello),
]