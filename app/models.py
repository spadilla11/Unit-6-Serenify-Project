from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    question_text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=300)
    incorrect_answers = models.JSONField()
    difficulty = models.CharField(max_length=50)
    api_source = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField()
    level = models.IntegerField()
    streak = models.IntegerField()
    total_time_studying = models.IntegerField()


    def __str__(self):
        return f"{self.user.username} Stats"

class StudyRoom(models.model):
    room_type = models.CharField(max_length=25)
    current_timer = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.room_type} Study Room"


class StudySession(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=25)
    minutes = models.IntegerField()
    date = models.DateTimeField()
    xp_earned = UserStats.xp()
    
    def __str__(self):
        return f"{self.room} Study Session"


class Task(models.model):
    title = models.CharField(max_length=25)
    subject = models.CharField()
    due_date = models.DateField()
    status = models.CharField()
    progress = models.IntegerField()

    def __str__(self):
        return f"{self.title} Task"


class Flashcard(models.model):
    subject = models.CharField(max_length=25)
    question = models.TextField(max_length=300)
    answer = models.TextField(max_length=200)
    last_reviewed = models.DateField()
    memory_strength = models.IntegerField()
    
    def __str__(self):
        return f"{self.subject} Flashcard"


class Achievement(models.model):
    name = models.CharField(max_length=25)
    xp_reward = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} Achievement"