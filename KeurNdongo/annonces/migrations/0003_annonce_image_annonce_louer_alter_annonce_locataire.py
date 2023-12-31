# Generated by Django 4.1 on 2023-08-17 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("annonces", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="annonce",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="images"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="annonce",
            name="louer",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="annonce",
            name="locataire",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="annonces_locataire",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
