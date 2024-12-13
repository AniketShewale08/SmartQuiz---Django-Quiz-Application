from django.urls  import path
from . import views
from django.contrib.auth import views as auth_views

app_name='quiz'
urlpatterns = [
    path('', views.home, name='home'),  # Home page to display quiz types
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('start/<int:quiz_type_id>/', views.StartQuizView.as_view(), name='start_quiz'),  # Pass quiz_type_id here
    path('submit_answer/<int:question_id>/', views.SubmitAnswerView.as_view(), name='submit_answer'),
    path('results/<int:quiz_type_id>/', views.QuizResultView.as_view(), name='quiz_results'),
    path('reset/<int:pk>/', views.ResetQuizView.as_view(), name='reset_quiz'),
]

# urlpatterns = [
#     path('', views.home, name='home'),  # Home page to display quiz types
#     # path('quiz/start/<int:quiz_type_id>/', views.start_quiz, name='start_quiz'),
#     path('register/', views.UserRegistrationView.as_view(), name='register'),
#     path('login/', views.LoginView.as_view(), name='login'),
#     # path('logout/', views.login_required, name='logout'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('start/', views.StartQuizView.as_view(), name='start_quiz'),
#     path('submit_answer/<int:question_id>/', views.SubmitAnswerView.as_view(), name='submit_answer'),
#     path('results/', views.QuizResultView.as_view(), name='quiz_results'),
#     path('reset/', views.ResetQuizView.as_view(), name='reset_quiz'),
# ]

