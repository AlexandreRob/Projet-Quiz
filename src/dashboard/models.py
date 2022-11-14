# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Service(models.Model):
    codeService = models.CharField(max_length=5, blank=False, null=False, unique=True)
    intitule = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.codeService

class Employe(models.Model):
    matriculeEmploye = models.CharField(max_length=5, blank=False, null=False, unique=True)
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    dateDeNaissance = models.CharField(max_length=50, blank=True, null=True)
    codePostalDeNaissance = models.CharField(max_length=5, blank=True, null=True)
    adresse1 = models.CharField(max_length=100, blank=True, null=True)
    adresse2 = models.CharField(max_length=100, blank=True, null=True)
    codePostal = models.CharField(max_length=5, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    idService = models.ForeignKey(Service, models.DO_NOTHING)

    def __str__(self):
        return self.matriculeEmploye

class Quiz(models.Model):
    intituleQuiz = models.CharField(max_length=5, blank=False, null=False)
    noteMini = models.IntegerField(blank=True, null=True)
    lienXml = models.CharField(max_length=500, blank=True, null=True)
    idService = models.ForeignKey(Service, models.DO_NOTHING)
    # idSession = models.OneToOneField(Session, models.DO_NOTHING)

    def __str__(self):
        return self.intituleQuiz
    

class Session(models.Model):
    intituleSession = models.CharField(max_length=50, blank=False, null=False)
    datedebutsession = models.DateTimeField(blank=True, null=True)
    datefinsession = models.DateTimeField(blank=True, null=True) 
    idService = models.ForeignKey(Service, models.DO_NOTHING)
    idEmploye = models.ForeignKey(Employe, models.DO_NOTHING)
    # idQuiz = models.ForeignKey(Quiz, models.DO_NOTHING)

    def __str__(self):
        return self.intituleSession

class Question(models.Model):
    titre = models.CharField(max_length=100, blank=True, null=True)
    intitule = models.CharField(max_length=100, blank=False, null=False)
    bonneReponse = models.IntegerField(blank=False, null=False)
    timer = models.DurationField(blank=True, null=True)
    coefficient = models.IntegerField(blank=False, null=False)
    feedback = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.intitule

class Reponse(models.Model):
    bonneReponse = models.BooleanField(blank=True, null=True)
    intituleReponse = models.CharField(max_length=100, blank=False, null=False)
    idQuestion = models.ForeignKey(Question, models.DO_NOTHING)

    def __str__(self):
        return self.intituleReponse

class Composer(models.Model):
    idQuiz = models.ForeignKey(Quiz, models.DO_NOTHING)
    idQuestion = models.ForeignKey(Question, models.DO_NOTHING)

class Constituer(models.Model):
    idReponse = models.ForeignKey(Reponse, models.DO_NOTHING)
    idQuestion = models.ForeignKey(Question, models.DO_NOTHING)

# class Posseder(models.Model):
#     idEmploye = models.OneToOneField(Employe, models.DO_NOTHING)
#     idService = models.ForeignKey(Service, models.DO_NOTHING)