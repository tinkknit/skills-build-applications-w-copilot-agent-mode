from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Spider-Man', 'Captain America'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')

        # Create activities
        Activity.objects.create(user='ironman@marvel.com', type='run', duration=30, date='2026-02-16')
        Activity.objects.create(user='spiderman@marvel.com', type='cycle', duration=45, date='2026-02-15')
        Activity.objects.create(user='superman@dc.com', type='swim', duration=60, date='2026-02-14')
        Activity.objects.create(user='batman@dc.com', type='walk', duration=20, date='2026-02-13')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
