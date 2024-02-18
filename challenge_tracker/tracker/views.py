from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Challenge, Task

def index(request):
    challenges = Challenge.objects.all
    template = loader.get_template("tracker/index.html")
    context = {
        "challenges": challenges,
    }
    return HttpResponse(template.render(context, request))

def all_challenges_tasks(request):
    # Retrieve all challenges
    challenges = Challenge.objects.all()

    # Create a dictionary to store tasks for each challenge
    challenge_tasks = {}
    for challenge in challenges:
        tasks = Task.objects.filter(challenge=challenge)
        challenge_tasks[challenge] = tasks

    return render(request, 'tracker/all_challenges_tasks.html', {'challenge_tasks': challenge_tasks})




