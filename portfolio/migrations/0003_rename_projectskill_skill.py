# Generated by Django 5.0.4 on 2024-05-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_description_en_project_description_fr_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectSkill',
            new_name='Skill',
        ),
    ]
