# Generated by Django 5.0.1 on 2024-09-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_marketmanager_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketmanager',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
