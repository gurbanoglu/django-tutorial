from django.urls import path
from . import views

# Set the application namespace.
app_name = "polls"

urlpatterns = [
  # ex: /polls/
  path("", views.index, name="index"),

  # ex: /polls/specifics/1/
  path("specifics/<int:question_id>/", views.detail, name="detail"),

  # ex: /polls/1/results/
  path("<int:question_id>/results/", views.results, name="results"),

  # ex: /polls/1/vote/
  # This request will be handled by the
  # vote() function in polls/views.py.
  path("<int:question_id>/vote/", views.vote, name="vote")
]