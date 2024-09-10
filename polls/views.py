from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import Http404

from .models import Choice, Question


def index(request):
  # order_by() is used to sort query sets.
  # [:5] is called slicing in Python. It means return the
  # first five Question objects in this context.
  latest_question_list = Question.objects.order_by("-pub_date")[:5]

  # Dictionary data structure
  context = {
    "latest_question_list": latest_question_list,
  }
  return render(request, "polls/index.html", context)


def detail(request, question_id):
  # Get a particular Question object based on its primary
  # key (pk).

  # http://127.0.0.1:8000/polls/specifics/1/

  # It raises Http404 if the object doesn’t exist.
  question = get_object_or_404(Question, pk=question_id)

  # Why is this here? Does this do the same as the previous line?
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)


# def vote(request, question_id):
#   return HttpResponse("You're voting on question %s." % question_id)

# The vote() function is invoked when making
# a POST request to the following URL:
# http://127.0.0.1:8000/polls/1/vote/
def vote(request, question_id):
  # In this case, question_id will be equal to
  # 1 because it is included in the URL.
  print("\nEntered vote() function in the polls/views.py module.")

  # Attempt to get a Question object from the
  # database based on the "question_id" attribute.
  # Raise an Http404 exception if not found.
  question = get_object_or_404(Question, pk=question_id)

  # The Question object will be the one in the database
  # that has a primary key equal to the value of the
  # question_id parameter.
  print("question:", question)

  print("\nBefore form submission")

  print("\nrequest:", request)

  print("\nrequest.POST:", request.POST)

  print('\nrequest.POST["choice"]:', request.POST.get("choice"))

  # The program enters the try block only after the form
  # is submitted.
  try:
    # request.POST is a dictionary-like object that lets
    # you access submitted data by key name. In this case,
    # request.POST['choice'] returns the ID of the selected
    # choice, as a string. request.POST values are always strings.

    # choice_set will return the Choice objects that belong to
    # this particular Question object.

    # The get() method will grab the one whose primary key is
    # equal to the ID of the selected Choice object which is
    # the value returned by request.POST["choice"].

    # The primary key is identified using the "choice" key coming
    # from the request.POST dictionary.
    selected_choice = question.choice_set.get(pk=request.POST["choice"])

    print("\nAfter form submission")

    print("request:", request)

    print("request.POST:", request.POST)

    print('request.POST["choice"]:', request.POST.get("choice"))

    print("selected_choice:", selected_choice)

  # request.POST['choice'] will raise a KeyError
  # if "choice" wasn’t provided in POST data.
  # Assign something other than "choice" to <input> element's
  # "name" attribute in polls/templates/polls/detail.html.

  # The above code checks for KeyError and redisplays the
  # question form with an error message if choice isn’t given.
  except (KeyError, Choice.DoesNotExist):
    print("KeyError raised.")

    # Re-display the question voting form.
    return render(
      request,
      "polls/detail.html",
      {
        "question": question,
        "error_message": "You didn't select a choice.",
      },
    )
  else:
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))