from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=16)
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=17)

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[{"email": user1.email}, {"email": user2.email}])

        # Create test activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-10")
        Activity.objects.create(user=user2, activity_type="Walking", duration=45, date="2025-04-10")

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        # Create test workouts
        Workout.objects.create(name="Push-ups", description="Do 20 push-ups", difficulty="Easy")
        Workout.objects.create(name="Squats", description="Do 15 squats", difficulty="Medium")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
