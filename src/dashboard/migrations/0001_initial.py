# Generated by Django 4.1.3 on 2022-11-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("matriculeEmploye", models.CharField(max_length=5, unique=True)),
                ("nom", models.CharField(max_length=50)),
                ("prenom", models.CharField(max_length=50)),
                (
                    "dateDeNaissance",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "codePostalDeNaissance",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("adresse1", models.CharField(blank=True, max_length=100, null=True)),
                ("adresse2", models.CharField(blank=True, max_length=100, null=True)),
                ("codePostal", models.CharField(blank=True, max_length=5, null=True)),
                ("ville", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(blank=True, max_length=100, null=True)),
                ("intitule", models.CharField(max_length=100)),
                ("bonneReponse", models.IntegerField()),
                ("timer", models.DurationField(blank=True, null=True)),
                ("coefficient", models.IntegerField()),
                ("feedback", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codeService", models.CharField(max_length=5)),
                ("intitule", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intituleSession", models.CharField(max_length=50)),
                ("datedebutsession", models.DateTimeField(blank=True, null=True)),
                ("datefinsession", models.DateTimeField(blank=True, null=True)),
                (
                    "idEmploye",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.employe",
                    ),
                ),
                (
                    "idService",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.service",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bonneReponse", models.BooleanField(blank=True, null=True)),
                ("intituleReponse", models.CharField(max_length=100)),
                (
                    "idQuestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intituleQuiz", models.CharField(max_length=5)),
                ("noteMini", models.IntegerField(blank=True, null=True)),
                ("lienXml", models.CharField(max_length=500)),
                (
                    "idService",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.service",
                    ),
                ),
                (
                    "idSession",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.session",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employe",
            name="idService",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="dashboard.service"
            ),
        ),
        migrations.CreateModel(
            name="Constituer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "idQuestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.question",
                    ),
                ),
                (
                    "idReponse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.reponse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Composer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "idQuestion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.question",
                    ),
                ),
                (
                    "idQuiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.quiz",
                    ),
                ),
            ],
        ),
    ]
