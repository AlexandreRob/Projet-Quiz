from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('sessions/', views.all_sessions, name="list-sessions"),
    path('add_session/', views.add_session, name="add-session"),
    path('add_question/', views.add_question, name="add-question"),
    # path('service_sessions/', views.service_sessions, name="service-sessions"),
]