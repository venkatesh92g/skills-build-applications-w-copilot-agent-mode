from djongo import models
from django.db.models import JSONField
from bson import ObjectId  # Import ObjectId for MongoDB compatibility

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # MongoDB ObjectId
    username = models.CharField(max_length=255, unique=True)  # Add username field
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=255)

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)  # Add default value for `_id`
    name = models.CharField(max_length=255)
    members = JSONField()  # Store list of members

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()