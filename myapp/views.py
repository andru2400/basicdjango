import imp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse("Hello index")

def about(request):
    return HttpResponse("About")

def hello(request, example):
    return HttpResponse("<h2>Hello Word %s </h2>" % example)

def hellonumber(request, example):
    print(type(example))
    return HttpResponse("<h2>Hello Number %s </h2>" % example)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)

def tasks(request,id):
    # task = Task.objects.get(id=id) 
    task = get_object_or_404(Task, id=id)                      # De Esta manera no renorna un error, si no que lanza un Codigo 404
    return HttpResponse("task: %s" %task.title)
    

