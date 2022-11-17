from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import QuestionsForm, SessionForm
from dashboard.models import Employe, Service, Role
from django.contrib.auth.hashers import make_password
import csv

def home(request):
    return render(request, "dashboard/home.html", {})

def all_sessions(request):
    session_list = Session.objects.all()
    nb_session = Session.objects.all().count
    nb_quizz = Quiz.objects.all().count
    nb_question = Question.objects.all().count
    return render(request, "dashboard/session_list.html",
        {"session_list": session_list,
         "nb_session": nb_session,
         "nb_quizz": nb_quizz,
         "nb_question": nb_question,
       })

def add_session(request):
    submitted = False

    if request.method == "POST":
        print("Hi!")
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_session?submitted=True")
    else:
        form = SessionForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "dashboard/add_session.html",{"form" : form, "submitted" : submitted})


def add_question(request):
    submitted = False

    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_question?submitted=True")
    else:
        form = QuestionsForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "dashboard/add_question.html",{"form" : form, "submitted" : submitted})

def all_questions(request):
    nb_question = Question.objects.all().count
    question_list = Question.objects.all()
    return render(request, "dashboard/question_list.html",
        {"nb_question": nb_question,
         "question_list": question_list,
       })
    

def add_quiz(request):
    return render(request, "dashboard/add_quiz.html", {})

def upload_quiz(request):
    return render(request, "dashboard/upload_quiz.html", {})

def quizz(request):
    return render(request, "dashboard/quizz.html", {})

def get_secteur(elements, secteur):
    code_secteur = elements[0]
    nom_secteur = elements[1]
    secteur["details"] = {}
    secteur["details"]["code_secteur"] = code_secteur
    secteur["details"]["nom_secteur"] = nom_secteur

def get_infos_chef_secteur(elements, secteur):
    matricule_chef_secteur = elements[2]
    nom_chef_secteur = elements[3]
    prenom_chef_secteur = elements[4]
    secteur["chef"] = {}
    secteur["chef"]["matricule"] = matricule_chef_secteur
    secteur["chef"]["nom"] = nom_chef_secteur
    secteur["chef"]["prenom"] = prenom_chef_secteur

def get_infos_collaborateur(elements, secteur):
    matricule_collaborateur = elements[5]
    nom_collaborateur = elements[6]
    prenom_collaborateur = elements[7]
    secteur["collaborateurs"].append({
        "matricule": matricule_collaborateur,
        "nom": nom_collaborateur,
        "prenom": prenom_collaborateur
    })

def create_secteur(secteur):
    code_secteur = secteur["details"]["code_secteur"]
    nom_secteur = secteur["details"]["nom_secteur"]

    secteur_a_creer = Service.objects.filter(pk=code_secteur)

    if not secteur_a_creer.exists(): # si le secteur n'existe pas en base de données,
        # on le crée
        Service.objects.create(codeService=code_secteur, intitule=nom_secteur)

def create_chef_secteur(secteur):
    mot_de_passe = make_password("azerty")
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "chef"
    username = secteur["chef"]["matricule"]
    matricule = secteur["chef"]["matricule"]
    nom = secteur["chef"]["nom"]
    prenom = secteur["chef"]["prenom"]

    chef_secteur = Employe.objects.filter(codeService=code_secteur, codeRole_id=code_role)

    if chef_secteur.exists():
        chef_secteur_actuel = chef_secteur.first()

        if chef_secteur_actuel.matriculeEmploye != matricule: # le chef de secteur actuel n'est pas celui présenté sur le csv
            # le chef de secteur actuel est passé en collaborateur
            chef_secteur_actuel.codeRole = Role.objects.get(pk="collab")
            chef_secteur_actuel.save()

            # on crée l'employé en tant que chef de secteur
            Employe.objects.create(username=username, password=mot_de_passe, matriculeEmploye=matricule, first_name=prenom, last_name=nom, codeService=Service.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))
    else:
        # on crée l'employé en tant que chef de secteur
        Employe.objects.create(username=username, password=mot_de_passe, matriculeEmploye=matricule, first_name=prenom, last_name=nom, codeService=Service.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))

def create_collaborateurs(secteur):
    mot_de_passe = make_password("azerty")
    code_secteur = secteur["details"]["code_secteur"]
    code_role = "collab"
    nouveaux_collaborateurs = secteur["collaborateurs"]

    anciens_collaborateurs = Employe.objects.filter(codeService=code_secteur, codeRole_id=code_role)
    if anciens_collaborateurs.exists(): # si il existe des collaborateurs dans le secteur sélectionné
        # on les efface de la base de données
        for ancien_collaborateur in anciens_collaborateurs:
            ancien_collaborateur.delete()
    
    # on crée les collaborateurs présents sur le csv
    for nouveau_collaborateur in nouveaux_collaborateurs:
        username = nouveau_collaborateur["matricule"]
        matricule = nouveau_collaborateur["matricule"]
        prenom = nouveau_collaborateur["prenom"]
        nom = nouveau_collaborateur["nom"]

        Employe.objects.create(username=username, password=mot_de_passe, matriculeEmploye=matricule, first_name=prenom, last_name=nom, codeService=Service.objects.get(pk=code_secteur), codeRole=Role.objects.get(pk=code_role))

def page_csv(request):
    if request.method == "POST":
        
        nom_fichier = request.POST["csv"]
        secteur = {}

        with open("D:/Documents/Afpar exo/" + nom_fichier, 'r', newline='') as f:
            reader = csv.reader(f)
            secteur["collaborateurs"] = []
            for index, row in enumerate(reader):
                elements = row[0].split(";")
                if index == 1:
                    get_secteur(elements, secteur)
                    get_infos_chef_secteur(elements, secteur)
                    get_infos_collaborateur(elements, secteur)
                elif index > 1:
                    get_infos_collaborateur(elements, secteur)
        create_secteur(secteur)
        create_chef_secteur(secteur)
        create_collaborateurs(secteur)
    return render(request, "dashboard/import_csv.html", {})


def quizz_list(request):
    return render(request, "dashboard/quizz_list.html", {})
