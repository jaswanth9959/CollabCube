from django.urls import path
from . import views

urlpatterns=[
    path('',views.projects,name="projects"),
    path('project/<str:pk>',views.project,name="project"),
    path('create-project/',views.createProject, name="create-project"),
    path('update-project/<str:pk>/',views.updateProject, name="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),
    path('create-resume/',views.createResume,name="create-resume"),
    path('resume/<str:pk>',views.resume,name="resume"),
    path('update-resume/<str:pk>',views.updateResume,name="update-resume"),
    path('delete-resume/<str:pk>',views.deleteResume,name="delete-resume"),
]