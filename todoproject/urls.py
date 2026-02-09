"""
Project-level URL configuration.
This is the "main router" - it directs traffic to each app's own urls.py
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Built-in admin panel at /admin/
    path('admin/', admin.site.urls),

    # Hand off to todos app's urls.py for everything else
    # include() means "go check todos/urls.py for more specific routes"
    path('', include('todos.urls')),
]

