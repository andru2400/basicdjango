from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:example>', views.hello),
    path('hellon/<int:example>', views.hellonumber),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    # path('tasks/<int:id>', views.tasks)
]