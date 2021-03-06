from django.shortcuts import render, redirect
from ordo .models import Room, Message
from django.http import HttpResponse, JsonResponse
from . models import *
from .forms import *


# Create your views here.
def index(request):
    meetings = Meetings.objects.all()
    context = {'meetings': meetings}

    return render(request, 'main/index.html', context)


def meetings(request):
    meets = Meets.objects.all()
    context = {'meets': meets}

    return render(request, 'main/meetings.html', context)


def community(request):
    return render(request, 'main/community.html')



def wiki(request):
    return render(request, 'main/wiki.html')


def forum_home(request):
    context = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context["dataset"] = User.objects.all()
    context['form'] = form
    return render(request, 'main/forum-home.html',context)


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'main/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})



def about_us(request):
    return render(request, 'main/about_us.html')


