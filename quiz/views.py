from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import  login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question, QuizSession, QuizType

def home(request):
    quiz_types = QuizType.objects.all()  
    return render(request, 'home.html', {'quiz_types': quiz_types})

class UserRegistrationView(SuccessMessageMixin, FormView):
    template_name = 'quiz/registration.html' 
    form_class = RegistrationForm
    success_url = reverse_lazy('quiz:login')  
    success_message = "Registration Successful! You can log in."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your registration.")
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = 'quiz/login.html'
    form_class = AuthenticationForm
    success_url = '/'
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form
    
class StartQuizView(LoginRequiredMixin, View):
    def get(self, request, quiz_type_id):
        try:
            quiz_type = QuizType.objects.get(id=quiz_type_id)  
        except QuizType.DoesNotExist:
            messages.error(request, "The requested quiz type does not exist.")
            return redirect('quiz:home')
        
        answered_questions = QuizSession.objects.filter(user=request.user).values_list('question_id', flat=True)
    
        remaining_questions = Question.objects.filter(quiz_type=quiz_type).exclude(id__in=answered_questions)
        
        if remaining_questions.exists():
            question = remaining_questions.order_by('?').first()
            return render(request, 'quiz/start_quiz.html', {'question': question, 'quiz_type': quiz_type})
        else:
            messages.info(request, "You have completed the quiz.")
            return redirect('quiz:quiz_results', quiz_type_id=quiz_type_id)

class SubmitAnswerView(LoginRequiredMixin, View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        quiz_type_id = question.quiz_type.id  
        selected_answer = request.POST.get('answer')

        if not selected_answer:
            messages.error(request, "You must select an answer.")
            return redirect('quiz:start_quiz', quiz_type_id=quiz_type_id)

        is_correct = selected_answer == question.correct_answer
        QuizSession.objects.create(
            user=request.user,
            question=question,
            selected_answer=selected_answer,
            is_correct=is_correct
        )

        answered_questions = QuizSession.objects.filter(user=request.user).values_list('question_id', flat=True)
        remaining_questions = Question.objects.filter(quiz_type=question.quiz_type).exclude(id__in=answered_questions)

        if remaining_questions.exists():
            return redirect('quiz:start_quiz', quiz_type_id=quiz_type_id)
        else:
            return redirect('quiz:quiz_results', quiz_type_id=quiz_type_id)
class QuizResultView(LoginRequiredMixin, View):
    def get(self, request, quiz_type_id):
      
        quiz_type = get_object_or_404(QuizType, id=quiz_type_id)
        quiz_sessions = QuizSession.objects.filter(user=request.user, question__quiz_type=quiz_type)

        correct_answers = quiz_sessions.filter(is_correct=True).count()
        incorrect_answers = quiz_sessions.filter(is_correct=False).count()
        total_questions = quiz_sessions.count()
        return render(request, 'quiz/quiz_results.html', {
            'quiz_type': quiz_type,
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'total_questions': total_questions,
            'quiz_sessions': quiz_sessions,
        })

class ResetQuizView(LoginRequiredMixin, View):
    def get(self, request, pk):
        quiz_type = get_object_or_404(QuizType, id=pk)
        QuizSession.objects.filter(user=request.user, question__quiz_type=quiz_type).delete()
        messages.success(request, f"Quiz '{quiz_type.name}' has been reset successfully.")
        return redirect('quiz:home')
