# Generated by Django 5.0.1 on 2024-09-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_marketmanager_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketmanager',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
