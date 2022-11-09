# Projet-Quiz
# Installation :
- Installer un environnement virtuel : ``py -m venv .env``
- Lancer l'environnement virtuel : ``.env\Scripts\activate.bat``
- Installer les différents packages (Django, ...) : ``pip install -r requirements.txt``
- Crée la base de donnée sur postgres avec les infos disponible dans le dossier quiz > fichier settings.py
- Crée un nouveau login dans postgres avec nom moni et mdp moni, mettre tout les privilèges
- Effectuer les premières migrations : ``cd src`` puis ``py manage.py makemigrations`` et ``py manage.py migrate``

# Lancer serveur Django
- Vérifier que l'environnement virtuel est lancé et que vous êtes bien dans le dossier 'src' : ``py manage.py runserver``
