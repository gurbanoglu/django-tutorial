from django.contrib import admin

# Register the models inside polls/admin.py, so
# that the "polls" app and its models appear on
# the admin page.
from .models import Question, Choice

admin.site.register(Question)

admin.site.register(Choice)