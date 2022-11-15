from django import forms
from django.forms import ModelForm
from .models import *

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ("id", "intituleSession", "dateDebutSession", "dateFinSession", "idService", "idQuiz")
    
        labels = {
            "intituleSession" : "",
            "dateDebutSession" : "YYYY-MM-DD HH:MM:SS",
            "dateFinSession" : "",
            "idService" : "",
            "idQuiz" : "",

        }
        widgets = {
            "intituleSession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer l'intitulé de la session"}),
            "dateDebutSession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de début"}),
            "dateFinSession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de fin"}),
            "idService" : forms.Select(attrs={"class":"form-select", 'placeholder' : "Entrer le service concerné"}),
            "idQuiz" : forms.Select(attrs={"class":"form-select", 'placeholder' : "Entrer le Quiz"}),
        }

class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ('id', "intitule", "titre", "coefficient", "timer", "bonneReponse", "feedback")
        labels = {
            "intitule" : "",
            "titre" : "",
            "coefficient" : "",
            "timer" : "",
            "bonneReponse" : "",
            "feedback" : "",
        }
        widgets = {
            "intitule" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer l'intitulé"}),
            "titre" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le titre de la question"}),
            "coefficient" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le coefficient"}),
            "timer" : forms.TimeInput(attrs={"class":"form-control", 'placeholder' : "Entrer le timer"}),
            "bonneReponse" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la bonne réponse"}),
            "feedback" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer un feedback"}),
        }
