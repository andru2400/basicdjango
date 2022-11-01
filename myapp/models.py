from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(max_length=200)     
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        # return self.title
        return self.title + ' - ' + self.project.name
