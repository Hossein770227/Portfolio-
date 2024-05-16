# Generated by Django 5.0.4 on 2024-05-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_skills_date_time_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name of course')),
                ('course', models.CharField(max_length=150, verbose_name='course')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('date_time_create', models.DateTimeField(auto_now_add=True, verbose_name='date time created')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'other skills',
                'verbose_name_plural': 'other skills',
            },
        ),
        migrations.AlterField(
            model_name='skills',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]