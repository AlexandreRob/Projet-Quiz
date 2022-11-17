from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('sessions/', views.all_sessions, name="list-sessions"),
    path('add_session/', views.add_session, name="add-session"),
    path('add_question/', views.add_question, name="add-question"),
    path('add_quiz/', views.add_quiz, name="add-quiz"),
    path('upload_quiz/', views.upload_quiz, name="upload-quiz"),
    path('quizz/', views.quizz, name='quizz'),
    path('quizz_list/', views.quizz_list, name='quizz_list'),
    path('question_list', views.all_questions, name='question_list'),
    path('page_csv/', views.page_csv, name='page-csv'),
    # path('service_sessions/', views.service_sessions, name="service-sessions"),
]