from django.urls import path

app_name = 'teams'

urlpatterns = [
    path('', lambda request: __import__('octofit_tracker.views').views.TeamListView.as_view()(request), name='team-list'),
]