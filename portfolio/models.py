from django.db import models


class ProjectSkill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Project(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField('short description', max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    skills = models.ManyToManyField(ProjectSkill)

    def __str__(self):
        return self.title


class ProjectLink(models.Model):
    label = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
