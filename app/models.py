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
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    total_time_studying = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.user} Stats"


class StudyRoom(models.Model):
    room_types = [('solo', 'Solo'),
                ('duel', 'Duel'),
                ('group', 'Group'),
                ('private', 'Private')]
    name = models.CharField(max_length=25)
    type_of_room = models.CharField(max_length=20, choices=room_types)
    current_timer = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # participants = models.ManyToManyField(User)
    
    def __str__(self):
        return f"{self.room_type} Study Room"


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(StudyRoom, on_delete=models.CASCADE)
    minutes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    xp_earned = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.room} Study Session"


class Task(models.Model):
    title = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)
    due_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} Task"


class Flashcard(models.Model):
    subject = models.CharField(max_length=25)
    question = models.TextField(max_length=300)
    answer = models.TextField(max_length=200)
    last_reviewed = models.DateField()
    memory_strength = models.IntegerField()
    
    def __str__(self):
        return f"{self.subject} Flashcard"


class Achievement(models.Model):
    name = models.CharField(max_length=25)
    xp_reward = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} Achievement"


class UserProfile(models.Model):
    pass