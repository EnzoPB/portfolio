# Generated by Django 5.0.4 on 2024-05-14 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_skill_detail_en_skill_detail_fr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(related_name='projects', to='portfolio.skill'),
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='portfolio.project'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='portfolio.skillcategory'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='detail_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='detail_fr',
            field=models.TextField(null=True),
        ),
    ]
