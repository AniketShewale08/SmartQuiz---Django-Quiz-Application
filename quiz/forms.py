from django import forms
from .models import QuizType, Question

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizType
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if QuizType.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A quiz with this name already exists.")        
        return name
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

    def clean_question_text(self):
        question_text = self.cleaned_data.get('question_text')
        if Question.objects.filter(question_text=question_text).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Question already exists.")
        return question_text