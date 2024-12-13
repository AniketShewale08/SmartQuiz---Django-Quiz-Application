from django.contrib import admin
from .models import Question, QuizSession, QuizType
# Register your models here.
admin.site.register(Question)
admin.site.register(QuizSession)
admin.site.register(QuizType)
