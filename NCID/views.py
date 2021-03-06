from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC, User
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone


class NCID_ListView(ListView):
    model = NPC
    template_name = 'NCID/NPC_list.html'
    paginate_by = 5

    def get_queryset(self):
        return NPC.objects.order_by('-time')


def search(request):
    blogs = NPC.objects.all().order_by('-time')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'NCID/search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'NCID/search.html')


def NCID_CreateView(request):
    if request.method == "POST":
        npc = NPC()
        npc.author = request.user.username
        npc.title = request.POST["title"]
        npc.contents = request.POST["contents"]
        npc.time = timezone.datetime.now()
        npc.file = request.FILES['file']
        npc.save()
        return redirect('list')
    return render(request, 'NCID/NPC_add.html')


class NCID_DetailView(DetailView):
    model = NPC
    template_name = 'NCID/NPC_detail.html'


def NCID_UpdateView(request, pk):
    npc = NPC.objects.get(pk=pk)
    if request.method == "POST":
        npc.title = request.POST['title']
        npc.contents = request.POST['contents']
        npc.file = request.POST['file']
        npc.time = timezone.datetime.now()
        npc.save()
        return redirect('list')
    return render(request, 'NCID/NPC_update.html', {'npc': npc})


def NCID_DeleteView(request, pk):
    ncid = NPC.objects.get(pk=pk)
    ncid.delete()
    return redirect('list')

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["repassword"]:
            student_id = request.POST['student_id']
            name = request.POST['name']
            password = request.POST['password']
            user = User.objects.create_user(student_id, name, password)
            user.is_active = False
            auth.login(request, user)
            return redirect('list')
        return redirect('signup')

    return render(request, 'NCID/signup.html')


def login(request):
    if request.method == 'POST':

        student_id = request.POST["student_id"]
        password = request.POST["password"]
        user = authenticate(request, username=student_id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            return render(request, 'NCID/login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'NCID/login.html')


def logout(request):
    auth.logout(request)
    return redirect('list')


def grade(request):
    return render(request, "NCID/grade.html")


