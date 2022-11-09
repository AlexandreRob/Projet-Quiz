# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'



class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Answers(models.Model):
    codeanswer = models.CharField(primary_key=True, max_length=50)
    answerlist = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'answers'


class AvoirAcces(models.Model):
    matriculeemployee = models.OneToOneField('Employees', models.DO_NOTHING, db_column='matriculeemployee', primary_key=True)
    codesession = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='codesession')

    class Meta:
        # managed = False
        db_table = 'avoir_acces'
        unique_together = (('matriculeemployee', 'codesession'),)


class Comporter(models.Model):
    codequizz = models.OneToOneField('Quizzes', models.DO_NOTHING, db_column='codequizz', primary_key=True)
    codesession = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='codesession')

    class Meta:
        # managed = False
        db_table = 'comporter'
        unique_together = (('codequizz', 'codesession'),)


class Composer(models.Model):
    codequizz = models.OneToOneField('Quizzes', models.DO_NOTHING, db_column='codequizz', primary_key=True)
    codequestion = models.ForeignKey('Questions', models.DO_NOTHING, db_column='codequestion')

    class Meta:
        # managed = False
        db_table = 'composer'
        unique_together = (('codequizz', 'codequestion'),)


class Constituer(models.Model):
    codequestion = models.OneToOneField('Questions', models.DO_NOTHING, db_column='codequestion', primary_key=True)
    codeanswer = models.ForeignKey(Answers, models.DO_NOTHING, db_column='codeanswer')

    class Meta:
        # managed = False
        db_table = 'constituer'
        unique_together = (('codequestion', 'codeanswer'),)


class Employees(models.Model):
    matriculeemployee = models.CharField(primary_key=True, max_length=4)
    mailemployee = models.CharField(max_length=50, blank=True, null=True)
    lastnameemployee = models.CharField(max_length=50, blank=True, null=True)
    telemployee = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    codeadmin = models.IntegerField(blank=True, null=True)
    codeservice = models.ForeignKey('Services', models.DO_NOTHING, db_column='codeservice')
    codejob = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='codejob')

    class Meta:
        # managed = False
        db_table = 'employees'


class Jobs(models.Model):
    codejob = models.CharField(primary_key=True, max_length=50)
    namejob = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'jobs'


class Posseder(models.Model):
    codeservice = models.OneToOneField('Services', models.DO_NOTHING, db_column='codeservice', primary_key=True)
    codejob = models.ForeignKey(Jobs, models.DO_NOTHING, db_column='codejob')

    class Meta:
        # managed = False
        db_table = 'posseder'
        unique_together = (('codeservice', 'codejob'),)


class Questions(models.Model):
    codequestion = models.CharField(primary_key=True, max_length=50, )
    titlequestion = models.CharField(max_length=50, blank=True, null=True)
    coeffquestion = models.CharField(max_length=50, blank=True, null=True)
    questionfeedback = models.CharField(max_length=50, blank=True, null=True)
    # imagequestion = models.BinaryField(blank=True, null=True)
    # questioncountdown = models.TimeField(blank=True, null=True)
    answeriscorrect = models.BooleanField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'questions'


class Quizzes(models.Model):
    codequizz = models.CharField(primary_key=True, max_length=50)
    namequizz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'quizzes'


class Resultats(models.Model):
    coderesult = models.IntegerField(primary_key=True)
    quizzresult = models.IntegerField(blank=True, null=True)
    dateresultt = models.DateTimeField(blank=True, null=True)
    codesession = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='codesession')

    class Meta:
        # managed = False
        db_table = 'resultats'


class Services(models.Model):
    codeservice = models.CharField(primary_key=True, max_length=50)
    nameservice = models.CharField(max_length=50,blank=True, null=True)
    # matriculeemployee = models.ForeignKey("Employees", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        # managed = False
        db_table = 'services'


class Sessions(models.Model):
    codesession = models.IntegerField(primary_key=True)
    datedebutsession = models.DateTimeField(blank=True, null=True)
    datefinsession = models.DateTimeField(blank=True, null=True)
    codeservice = models.ForeignKey(Services, models.DO_NOTHING, db_column='codeservice')
    # matriculeemployee = models.ForeignKey(AvoirAcces, models.DO_NOTHING, db_column='matriculeemployee')

    class Meta:
        # managed = False
        db_table = 'sessions'
