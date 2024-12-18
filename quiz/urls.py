from django.urls  import path
from . import views

app_name='quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('start/<int:quiz_type_id>/', views.StartQuizView.as_view(), name='start_quiz'),
    path('submit_answer/<int:question_id>/', views.SubmitAnswerView.as_view(), name='submit_answer'),
    path('results/<int:quiz_type_id>/', views.QuizResultView.as_view(), name='quiz_results'),
    path('reset/<int:pk>/', views.ResetQuizView.as_view(), name='reset_quiz'),
    path('manage-quiz/', views.manage_quiz, name="manage-quiz"),
    path('add-quiz/', views.add_quiz, name ="add_quiz"),
    path('update-quiz/<int:pk>/', views.update_quiz, name = "update_quiz"),
    path('delete-quiz/<int:pk>/', views.delete_quiz, name = "delete_quiz"),
    path('add-question/<int:pk>', views.add_questions, name='add_question'),
    path('update-question/<int:pk>', views.update_question, name="update_question"),
    path('delete-question/<int:pk>/', views.delete_question, name='delete_question'),
    path('questions/manage/<int:pk>/', views.manage_questions, name='manage_questions'),
]