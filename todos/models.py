"""
MODELS - Defines the data structure. This is the foundation that everything else builds on.
Flow: Models define what data exists -> Views query that data -> Templates display it.
"""
from django.db import models


class Todo(models.Model):
    """
    Each Todo becomes a row in the database.
    Inherits from models.Model which gives us save(), delete(), objects.all(), etc. This is creating a table 
    in the database called Todo which has certain fields (title, completed). 
    In order to create this table or update its attributes we'd need to make migrations then run migrations
    """
    # CharField = short text, max_length is required
    title = models.CharField(max_length=200)

    # BooleanField = True/False, default sets the initial value
    completed = models.BooleanField(default=False)

    def __str__(self):
        # Controls how this object displays as a string (e.g., in admin panel)
        return self.title

