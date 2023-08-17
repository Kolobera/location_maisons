# Generated by Django 4.1 on 2023-08-17 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("annonces", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="annonce",
            name="locataire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="annonces_locataire",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="annonce",
            name="proprietaire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="annonces_proprietaire",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]