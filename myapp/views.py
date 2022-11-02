import imp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    # return HttpResponse("Hello index")
    title = 'Django params example Back'
    return render(request,'index.html',{'title':title})

def about(request):
    # return HttpResponse("About")
     return render(request,'about.html')

def hello(request, example):
    return HttpResponse("<h2>Hello Word %s </h2>" % example)

def hellonumber(request, example):
    print(type(example))
    return HttpResponse("<h2>Hello Number %s </h2>" % example)

def projects(request):
    # projects = list(Project.objects.values())
    projects = list(Project.objects.all())
    # return JsonResponse(projects,safe=False)
    return render(request, 'projects.html',{
        'projects':projects
    })

# def tasks(request,id):
def tasks(request):
    # task = Task.objects.get(id=id) 
    # task = get_object_or_404(Task, id=id)                      # De Esta manera no renorna un error, si no que lanza un Codigo 404
    tasks = list(Task.objects.all())
    # return HttpResponse("task: %s" %task.title)
    return render(request, 'tasks.html',{
        'tasks':tasks
    })
    

