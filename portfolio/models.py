from django.db import models

from uuid import uuid4

def random_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{uuid4()}.{ext}'


class SkillCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill category'
        verbose_name_plural = 'Skill categories'

class Skill(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=100)
    icon = models.FileField(upload_to=random_filename)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

class Project(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField('short description', max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=random_filename)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


class ProjectLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon = models.FileField(upload_to=random_filename)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
