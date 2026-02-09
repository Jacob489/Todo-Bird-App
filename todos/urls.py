"""
URLS - The router. Maps URL patterns to view functions.
Flow: User visits URL -> urls.py matches pattern -> Calls the corresponding function from views.py.
"""
from django.urls import path
from . import views

# Each path() maps a URL pattern to a view function
# 'name' lets us reference the URL elsewhere (e.g., in templates with {% url 'name' %})
urlpatterns = [
    # '' = root URL of this app (e.g., /)
    path('', views.todo_list, name='todo_list'),

    # <int:todo_id> captures a number from the URL and passes it to the view
    # Example: /delete/5/ -> calls delete_todo(request, todo_id=5)
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
]