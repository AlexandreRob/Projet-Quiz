from django import forms
from django.forms import ModelForm
from .models import *

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ("id", "intituleSession", "datedebutsession", "datefinsession", "idService", "idEmploye")
    
        labels = {
            "intituleSession" : "",
            "datedebutsession" : "YYYY-MM-DD HH:MM:SS",
            "datefinsession" : "",
            "idService" : "Entrer le service",
            "idEmploye" : "Entrer l'employée",
        }
        widgets = {
            "intituleSession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer l'intitulé de la session"}),
            "datedebutsession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de début"}),
            "datefinsession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de fin"}),
            "idService" : forms.Select(attrs={"class":"form-select", 'placeholder' : "Entrer le service concerné"}),
            "idEmploye" : forms.Select(attrs={"class":"form-select", 'placeholder' : "Entrer l'employé concerné"}),
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
