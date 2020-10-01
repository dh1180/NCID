from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC, NPC_school
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth.models import User
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from django.http import JsonResponse

def school(request):
    NPC_school.objects.all().delete()
    driver = webdriver.Chrome("C:\\Users\\mjdh1\\Downloads\\chromedriver_win32\\chromedriver.exe")
    url = "https://school.iamservice.net/organization/10135/group/2015103"
    driver.get(url)
    web_page = driver.page_source
    soup = BeautifulSoup(web_page, "html.parser")
    select = soup.select(
        "div.newsList"
    )

    for i in select:
        NPC(
            contets = i[0].text
        ).save()

        return JsonResponse({'search list': list(NPC_school.objects.values())}, status=200)


# Create your views here.

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
    npc = NPC()
    npc.title = request.GET["title"]
    npc.contents = request.GET["contents"]
    npc.time = timezone.datetime.now()
    npc.save()
    return redirect('list')

def create(request):
    return render(request, 'NCID/NPC_add.html')

class NCID_DetailView(DetailView):
    model = NPC
    template_name = 'NCID/NPC_detail.html'

def NCID_UpdateView(request, pk):
    npc_all = NPC.objects.all()
    npc = NPC.objects.get(pk=pk)
    if request.method == "POST":
        npc.title = request.POST['title']
        npc.contents = request.POST['contents']
        npc.time = timezone.datetime.now()
        npc.save()
        return redirect('list')
    else:
        return render(request, 'NCID/NPC_update.html', {'npc_all': npc_all})


class NCID_DeleteView(DeleteView):
    model = NPC
    success_url = reverse_lazy('list')
    template_name = 'NCID/NPC_delete.html'

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

def university(request):
    return render(request, "NCID/university.html")

