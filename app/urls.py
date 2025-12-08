from django.urls import path, include
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('', landing_view, name="home"),
    path('admin/', admin.site.urls),
=======
    path('', landing_view, name='landing'),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
    path('home/', home_view, name="home"),
>>>>>>> 30463dd28f21a0d83453535e54132fc52a71487a
]