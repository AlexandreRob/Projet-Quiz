# Generated by Django 4.1.3 on 2022-11-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quiz", old_name="idService", new_name="codeService",
        ),
        migrations.RenameField(
            model_name="session", old_name="idService", new_name="codeService",
        ),
    ]