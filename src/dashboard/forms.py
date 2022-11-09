from django import forms
from django.forms import ModelForm
from .models import Questions, Sessions

class SessionForm(ModelForm):
    class Meta:
        model = Sessions
        fields = ("codesession", "datedebutsession", "datefinsession", "codeservice")
    
        labels = {
            "codesession" : "",
            "datedebutsession" : "YYYY-MM-DD HH:MM:SS",
            "datefinsession" : "",
            "codeservice" : "Entrer le service concerné",
        }
        widgets = {
            "codesession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le code"}),
            "datedebutsession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de début"}),
            "datefinsession" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer la date de fin"}),
            "codeservice" : forms.Select(attrs={"class":"form-select", 'placeholder' : "Entrer le service concerné"}),
        }

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ('codequestion', "titlequestion", "coeffquestion", "questionfeedback", "answeriscorrect")
        labels = {
            "codequestion" : "",
            "titlequestion" : "",
            "coeffquestion" : "",
            "questionfeedback" : "",
            # "questioncountdown" : "",
            "answeriscorrect" : "La bonne réponse",
        }
        widgets = {
            "codequestion" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le code"}),
            "titlequestion" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le titre de la question"}),
            "coeffquestion" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le coefficient"}),
            "questionfeedback" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer le feedback"}),
            # "questioncountdown" : forms.TextInput(attrs={"class":"form-control", 'placeholder' : "Entrer un décompte de temps"}),
            "answeriscorrect" : forms.CheckboxInput(attrs={"class":"form-chekbox", 'placeholder' : "La réponse est bonne ou pas"}),
        }