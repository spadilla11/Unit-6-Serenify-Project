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


    def __str__(self):
        return f"{self.user.username} Stats"