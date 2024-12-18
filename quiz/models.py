from django.db import models
from django.contrib.auth.models import User

class QuizType(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField()  

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz_type = models.ForeignKey(QuizType, related_name='questions', on_delete=models.CASCADE)  
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)
    
    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    STATUS_CHOICES = (
        ('attempted', 'Attempted'),
        ('unattempted', 'Unattempted'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])
    is_correct = models.BooleanField(default=False)
    status = models.CharField(max_length=12, choices = STATUS_CHOICES, default = 'unattempted')

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"
