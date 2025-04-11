from djongo import models
from djongo.models import ObjectIdField

class User(models.Model):
    id = ObjectIdField(primary_key=True)  # Explicitly use ObjectIdField for primary key
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    id = ObjectIdField(primary_key=True)  # Explicitly use ObjectIdField for primary key
    name = models.CharField(max_length=100)
    members = models.JSONField()  # Use JSONField to store user references as a list of dictionaries
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)  # Explicitly use ObjectIdField for primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)  # Explicitly use ObjectIdField for primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.user.email} - {self.points} points"

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)  # Explicitly use ObjectIdField for primary key
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name
