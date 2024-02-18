import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from tracker.models import Challenge, Task, Completion
from django.utils import timezone

def create_challenge():
    # Create a user (you may want to adjust this according to your actual user model)
    user = User.objects.create(username='fefe', email='fefe@gmail.com')
    user.set_password('welcome')
    user.save()

    # Create a challenge
    challenge = Challenge.objects.create(name='30-Day Challenge', description='Complete tasks every day for 30 days', created_by=user)

    # Create 30 tasks for the challenge
    for day in range(1, 31):
        task_name = f'Task {day}'
        task_description = f'Description for Task {day}'
        task = Task.objects.create(challenge=challenge, name=task_name, description=task_description)

    # Complete all tasks for the challenge (for demonstration purposes)
    for task in Task.objects.filter(challenge=challenge):
        completion = Completion.objects.create(task=task, user=user, completed_at=timezone.now(), comment=f'Completed {task.name}')

if __name__ == "__main__":
    create_challenge()
