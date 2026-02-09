"""
VIEWS - The brain. Receives requests, talks to the database, returns responses.
Flow: URLs route to a view -> View fetches/modifies data -> View picks a template -> HTML returned.
"""
from django.shortcuts import render, redirect
from .models import Todo


def todo_list(request):
    """
    Main view - displays all todos and handles adding new ones.
    GET request = show the page
    POST request = form was submitted, create new todo
    """
    if request.method == 'POST':
        # Get the 'title' field from the submitted form data
        title = request.POST.get('title')
        if title:
            # Create a new Todo in the database with that title
            Todo.objects.create(title=title)
        # Redirect back to this same page (prevents form resubmission on refresh)
        return redirect('todo_list')

    # For GET requests: fetch all todos and render the template
    todos = Todo.objects.all()
    # Third argument is the 'context' - data passed to the template, in this case the context is the dictionary of all existing todos
    return render(request, 'todos/todo_list.html', {'todos': todos})


def delete_todo(request, todo_id):
    """
    Deletes a todo by its ID.
    todo_id comes from the URL: /delete/5/ -> todo_id = 5
    """
    if request.method == 'POST':
        # .get(id=...) fetches one specific record from the database
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
    return redirect('todo_list')


def toggle_todo(request, todo_id):
    """
    Flips a todo between completed and not completed.
    """
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        # Flip the boolean: True becomes False, False becomes True
        todo.completed = not todo.completed
        # Must call .save() to write changes to the database
        todo.save()
    return redirect('todo_list')