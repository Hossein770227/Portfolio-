# Generated by Django 5.0.4 on 2024-05-08 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_rename_descrisption_skills_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'skills', 'verbose_name_plural': 'skills'},
        ),
    ]