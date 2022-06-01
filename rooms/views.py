from unicodedata import name
from django.shortcuts import redirect, render
from .models import Room, RoomMessage,Topic
from .forms import RoomForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = 'login')
def rooms(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|Q(name__icontains=q)|Q(host__name__icontains=q))
    topics = Topic.objects.all()[0:5]
    room_messages = RoomMessage.objects.filter(
        Q(room__topic__name__icontains=q))[0:3]
    room_count = rooms.count()

    context = {'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'rooms/rooms.html',context)

@login_required(login_url = 'login')
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.roommessage_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        message = RoomMessage.objects.create(
            user = request.user.profile,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user.profile)
        return redirect('room', pk=room.id)
    context = {'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'rooms/room.html',context)

@login_required(login_url = 'login')
def createRoom(request):
    profile = request.user.profile
    form = RoomForm()
    if request.method =='POST':
        topic_name = request.POST.get('topic')
        # print("TOPIC-"+topic_name)
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = profile
            topic, created = Topic.objects.get_or_create(name=topic_name)
            room.topic = topic
            room.save()
            
            # room.topic.add(topic)
            messages.success(request,'Room was created successfully')
            room = Room.objects.get(name=request.POST.get('name'))
            room.participants.add(profile)
            return redirect('room', pk=room.id)    
    context = {'form':form}
    return render(request,'rooms/room-form.html',context)

@login_required(login_url = 'login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            messages.success(request,'Room was updated successfully')
            return redirect('room', pk=room.id)
    context = {'form':form}
    return render(request,'rooms/room-form.html',context)

@login_required(login_url = 'login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request,'Room was deleted successfully')
        return redirect('rooms')
    context = {'object':room.name}
    return render(request,'delete-template.html',context)

@login_required(login_url = 'login')
def joinRoom(request,pk):
    room = Room.objects.get(id=pk)
    password = request.POST.get('password')
    if room.password == password:
        room.participants.add(request.user.profile)
        messages.success(request,'Joined the room successfully')
        return redirect('room', pk=room.id)
    elif password == None:
        pass
    else:
        messages.error(request,'Incorrect password!')
    context = {'room':room}
    return render(request,'rooms/joinroom.html',context)

@login_required(login_url = 'login')
def deleteMessage(request, pk):
    message = RoomMessage.objects.get(id=pk)
    room = message.room
    if request.user.profile != message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        return redirect('room', pk=room.id)
    return render(request, 'delete-template.html', {'object': message.body})

@login_required(login_url = 'login')
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'rooms/topic_comp.html', {'topics': topics})

@login_required(login_url = 'login')
def activityPage(request):
    room_messages = RoomMessage.objects.all()
    return render(request, 'rooms/activity_comp.html', {'room_messages': room_messages})