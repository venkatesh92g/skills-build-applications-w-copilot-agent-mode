from .activities import urlpatterns as activities_patterns
from .leaderboard import urlpatterns as leaderboard_patterns
from .teams import urlpatterns as teams_patterns
from .users import urlpatterns as users_patterns
from .workouts import urlpatterns as workouts_patterns

urlpatterns = []
urlpatterns += activities_patterns
urlpatterns += leaderboard_patterns
urlpatterns += teams_patterns
urlpatterns += users_patterns
urlpatterns += workouts_patterns