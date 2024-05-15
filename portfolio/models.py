from django.db import models

from uuid import uuid4

def random_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{uuid4()}.{ext}'

class Icon(models.Model):
    name = models.CharField(max_length=50)
    svg = models.TextField()

    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill category'
        verbose_name_plural = 'Skill categories'

class Skill(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True, related_name='skills')

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
    skills = models.ManyToManyField(Skill, related_name='projects')

    def __str__(self):
        return self.title


class ProjectLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
