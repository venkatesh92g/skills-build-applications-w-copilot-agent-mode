from django.urls import path

app_name = 'workouts'

urlpatterns = [
    path('', lambda request: __import__('octofit_tracker.views').views.WorkoutListView.as_view()(request), name='workout-list'),
]