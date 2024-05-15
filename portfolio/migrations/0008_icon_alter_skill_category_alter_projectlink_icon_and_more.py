# Generated by Django 5.0.4 on 2024-05-14 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_project_skills_alter_projectlink_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('svg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills', to='portfolio.skillcategory'),
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='icon'
        ),
        migrations.AddField(
            model_name='projectlink',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.icon'),
        ),
        migrations.RemoveField(
            model_name='skill',
            name='icon'
        ),
        migrations.AddField(
            model_name='skill',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.icon'),
        ),
    ]
