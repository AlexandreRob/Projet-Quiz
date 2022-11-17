from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import Role
from dashboard.models import Service
from dashboard.models import Employe
from django.contrib.auth.hashers import make_password

# Create your views here.
def create_roles():
    Role.objects.create(codeRole="admin", nomRole="administrateur")
    Role.objects.create(codeRole="chef", nomRole="chef de secteur")
    Role.objects.create(codeRole="collab", nomRole="collaborateur")

def create_secteurs():
    Service.objects.create(codeService="MKT", intitule="marketing")
    Service.objects.create(codeService="RD", intitule="recherche et développement")
    Service.objects.create(codeService="RH", intitule="ressources humaines")

def create_super_user():
    mot_de_passe = make_password("admin")
    cs = Service.objects.get(pk="MKT")
    cr = Role.objects.get(pk="admin")
    Employe.objects.create(username="admin", password=mot_de_passe, email="admin@example.com", is_superuser=True, is_staff=True, matriculeEmploye="AAAA", codeService=cs, codeRole=cr)

def create_chef_secteur(secteur):
    mot_de_passe = make_password("azerty")
    cs = Service.objects.get(pk=secteur)
    cr = Role.objects.get(pk="chef")
    Employe.objects.create(username="jean", password=mot_de_passe, email="jean@example.com", is_superuser=True, is_staff=True, matriculeEmploye="AAAB", codeService=cs, codeRole=cr)

def create_collaborateurs(secteur):
    mot_de_passe = make_password("azerty")
    cs = Service.objects.get(pk=secteur)
    cr = Role.objects.get(pk="collab")
    Employe.objects.create(username="jacques", password=mot_de_passe, email="jacques@example.com", matriculeEmploye="AAAC", codeService=cs, codeRole=cr)
    Employe.objects.create(username="marie", password=mot_de_passe, email="marie@example.com", matriculeEmploye="AAAD", codeService=cs, codeRole=cr)


def index(request):
    create_roles()
    # ---------------------------------------------------------------
    create_secteurs()
    # --------------------------- Création super user ---------------
    create_super_user()
    # --------------------------- Création chef secteur RD ----------
    create_chef_secteur("RD")
    # --------------------------- Création collaborateurs RD ---------
    create_collaborateurs("RD")
    # ------------------- test contrainte d'unicité matricule -------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="collab")
    # Utilisateur.objects.create(username="laurent", password=mot_de_passe, email="laurent@example.com", matricule="AAAC", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    # ------------------- test contrainte d'unicité role(chef)/secteur -------
    # mot_de_passe = make_password("azerty")
    # cs = Secteur.objects.get(pk="RD")
    # cm = Metier.objects.get(pk="dev_web")
    # cr = Role.objects.get(pk="chef")
    # Utilisateur.objects.create(username="paul", password=mot_de_passe, email="paul@example.com", matricule="AAAE", codeSecteur=cs, codeMetier=cm, codeRole=cr)
    return render(request, "login.html", {})





def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')     

        else:
            messages.success(request, 'Erreur, veuillez réessayez ...')
            return redirect('login')     
    
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté!!!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Utilisateur créé!'))
            return redirect('home')
    else:
        form = UserCreationForm()
   
    return render(request, 'authenticate/register_user.html',{
        'form': form,
        })