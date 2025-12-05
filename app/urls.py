from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', landing_view, name="home"),
    path('admin/', admin.site.urls),
]