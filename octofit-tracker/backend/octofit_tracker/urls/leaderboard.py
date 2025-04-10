from django.urls import path

app_name = 'leaderboard'

urlpatterns = [
    path('', lambda request: __import__('octofit_tracker.views').views.LeaderboardListView.as_view()(request), name='leaderboard-list'),
]