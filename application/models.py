from django.db import models


class Stack(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    portfolio_url = models.URLField(max_length=200)
    stack = models.ManyToManyField(Stack)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name



