from django.shortcuts import render,redirect
from django.contrib import messages
from projects.utils import searchprojects
from .models import Project,Tag, Resume
from .forms import ProjectForm, ReviewForm, ResumeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import paginateProjects

@login_required(login_url = 'login')
def projects(request):
    projects,search_query = searchprojects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context={'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,"projects/projects.html",context)

def project(request,pk):
    project= Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request,"Your review was succesfully added")
        return redirect('project', pk=project.id)
    context={'project':project,'form':form}
    return render(request,"projects/single-project.html",context)

@login_required(login_url = 'login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form':form}
    return render(request,"projects/project-form.html",context)


@login_required(login_url = 'login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(','," ").split()
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {'form':form,'project':project}
    return render(request,"projects/project-form.html",context)


@login_required(login_url = 'login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context={'object':project.title}
    return render(request,"delete-template.html",context)

@login_required(login_url='login')
def createResume(request):
    profile = request.user.profile
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = profile
            resume.save()
            return redirect('resume', pk=resume.id)
    context = {'form':form}
    return render(request,"projects/resume-form.html",context)

@login_required(login_url='login')
def updateResume(request,pk):
    profile = request.user.profile
    resume = profile.resume_set.get(id=pk)
    form = ResumeForm(instance=resume)
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES,instance=resume)
        if form.is_valid():
            resume = form.save()
            return redirect('resume', pk=resume.id)
    context = {'form':form,'resume':resume}
    return render(request,"projects/resume-form.html",context)

@login_required(login_url='login')
def deleteResume(request,pk):
    profile = request.user.profile
    resume = profile.resume_set.get(id=pk)
    if request.method == 'POST':
        resume.delete()
        return redirect('account')
    context={'object':resume.name}
    return render(request,"delete-template.html",context)

@login_required(login_url='login')
def resume(request,pk):
    resume = Resume.objects.get(id=pk)

    context = {'resume':resume}

    return render(request,"projects/single-resume.html",context)
