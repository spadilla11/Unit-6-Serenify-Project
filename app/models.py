from django.db import models

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
    

