from django.urls import path

app_name = 'activities'

urlpatterns = [
    path('', lambda request: __import__('octofit_tracker.views').views.ActivityListView.as_view()(request), name='activity-list'),
]