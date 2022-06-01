import imp
import profile
from django.shortcuts import render,redirect
from .utils import paginateProfiles
from users.utils import searchProfiles
from .models import Profile,Skill,Message,Announcement,Notes
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm,ProfileForm,SkillForm,MessageForm,AnnouncementForm,NotesForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


def loginUser(request):
    page = 'login'
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"Username does not exist!")
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')
        else:
            messages.error(request,"Username or Password is wrong!")

    return render(request,"users/login-register.html",context)

def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out!")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User account has been created!")
            login(request,user)
            return redirect('edit-account')
        else:
            messages.error(request,"User account was not created!")
    context = {'page':page, 'form':form}
    return render(request, "users/login-register.html",context)
@login_required(login_url="login")
def profiles(request):

    profiles , search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 6)
    context={'profiles':profiles,'search_query':search_query,'custom_range': custom_range}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id = pk)

    topskills = profile.skill_set.exclude(description__exact="")

    otherskills = profile.skill_set.filter(description__exact="")
    context = {'profile':profile,'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/user-profile.html',context)

@login_required(login_url = 'login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    announcements = profile.announcement_set.all()
    resumes = profile.resume_set.all()
    context = {'profile':profile,'skills':skills,'projects':projects,'resumes':resumes,'announcements':announcements}
    return render(request, 'users/account.html',context)

@login_required(login_url = 'login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance= profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {"form":form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,'Skill was added successfully')
            return redirect('account')
    context={'form':form}
    return render(request, 'users/skill_form.html',context)

@login_required(login_url='login')
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'Skill was updated successfully')
            return redirect('account')
    context={'form':form}
    return render(request, 'users/skill_form.html',context)


@login_required(login_url='login')
def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request,'Skill was deleted successfully')
        return redirect('account')
    context = {'object':skill.name}
    return render(request,'delete-template.html',context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadcount = messageRequests.filter(is_read = False).count()
    context = {'messageRequests':messageRequests,'unreadcount':unreadcount}
    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read= True
        message.save()
    context={'message':message}
    return render(request, 'users/message.html',context)


@login_required(login_url='login')
def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,'Your message is sent successfully')
            return redirect('user-profile',pk=recipient.id)

    context = {'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)

@login_required(login_url='login')
def announcements(request):
    announcements = Announcement.objects.all()
    context = {'announcements':announcements}
    return render(request,'users/announce.html',context)
@login_required(login_url='login')
def announcement(request,pk):
    announcement = Announcement.objects.get(id=pk)
    context = {'announcement':announcement}
    return render(request,'users/single-announce.html',context)

@login_required(login_url='login')
def createAnnouncement(request):
    profile = request.user.profile
    form = AnnouncementForm()
    if request.method =='POST':
        form = AnnouncementForm(request.POST,request.FILES)
        if form.is_valid():
            announce = form.save(commit= False)
            announce.owner = profile
            announce.save()
            messages.success(request,'Announcement was added successfully')
            return redirect('announcements')
    context={'form':form}
    return render(request, 'users/announce_form.html',context)
    
@login_required(login_url='login')
def updateAnnouncement(request,pk):
    profile = request.user.profile
    announce = profile.announcement_set.get(id=pk)
    form = AnnouncementForm(instance=announce)
    if request.method =='POST':
        form = AnnouncementForm(request.POST,request.FILES,instance=announce)
        if form.is_valid():
            announce = form.save(commit= False)
            announce.owner = profile
            announce.save()
            messages.success(request,'Announcement was updated successfully')
            return redirect('myAnnouncements')
    context={'form':form}
    return render(request, 'users/announce_form.html',context)

@login_required(login_url='login')
def deleteAnnouncement(request,pk):
    profile = request.user.profile
    announce = profile.announcement_set.get(id=pk)
    if request.method == 'POST':
        announce.delete()
        messages.success(request,'Announcement was deleted successfully')
        return redirect('myAnnouncements')
    context = {'object':announce.title}
    return render(request,'delete-template.html',context)

@login_required(login_url='login')
def myAnnouncements(request):
    profile = request.user.profile
    announce = profile.announcement_set.all()
    context = {'announcements':announce}
    return render(request,'users/myannouncements.html',context)



@login_required(login_url='login')
def notes(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    notes = Notes.objects.distinct().filter(Q(topic__icontains=search_query)|Q(subject__icontains=search_query))
    context = {'notes':notes,'search_query':search_query}
    return render(request,'users/notes.html',context)


@login_required(login_url='login')
def mynotes(request):
    profile = request.user.profile
    notes = profile.notes_set.all()
    if request.user.profile.role != "faculty":
        return HttpResponse('Your are not allowed here!!')
    context = {'notes':notes}
    return render(request,'users/mynotes.html',context)


@login_required(login_url='login')
def uploadnotes(request):
    profile = request.user.profile
    form = NotesForm()
    if request.user.profile.role != "faculty":
        return HttpResponse('Your are not allowed here!!')
    if request.method =='POST':
        form = NotesForm(request.POST,request.FILES)
        if form.is_valid():
            announce = form.save(commit= False)
            announce.owner = profile
            announce.save()
            messages.success(request,'Notes was added successfully')
            return redirect('notes')
    context={'form':form}
    return render(request, 'users/notes-form.html',context)


@login_required(login_url='login')
def editnotes(request,pk):
    profile = request.user.profile
    note = profile.notes_set.get(id=pk)
    form = NotesForm(instance=note)
    if request.user.profile.role != "faculty":
        return HttpResponse('Your are not allowed here!!')
    if request.method =='POST':
        form = NotesForm(request.POST,instance=note)
        if form.is_valid():
            note = form.save(commit= False)
            note.owner = profile
            note.save()
            messages.success(request,'Notes was updated successfully')
            return redirect('my-notes')
    context={'form':form}
    return render(request, 'users/notes-form.html',context)


@login_required(login_url='login')
def deletenotes(request,pk):
    profile = request.user.profile
    note = profile.notes_set.get(id=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request,'Notes was deleted successfully')
        return redirect('my-notes')
    context = {'object':note.topic}
    return render(request,'delete-template.html',context)