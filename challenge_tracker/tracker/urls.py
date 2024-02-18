from django.urls import path

from . import views


app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("all_challenges_tasks/", views.all_challenges_tasks, name="all_challenges_tasks"),
]