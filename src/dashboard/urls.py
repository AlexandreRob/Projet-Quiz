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
    path('list_question', views.all_questions, name='list-question'),
    path('import_csv', views.page_csv, name='import-csv')
    # path('service_sessions/', views.service_sessions, name="service-sessions"),
]