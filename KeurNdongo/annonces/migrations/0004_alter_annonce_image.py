# Generated by Django 4.2.1 on 2023-08-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0003_annonce_image_annonce_louer_alter_annonce_locataire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
