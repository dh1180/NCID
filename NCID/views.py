from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate

from django.contrib.auth.models import User



# Create your views here.

class NPC_ListView(ListView):
    model = NPC
    template_name = 'NCID/NPC_list.html'

class NPC_CreateView(CreateView):
    model = NPC
    template_name = 'NCID/NPC_add.html'
    fields = ['title', 'contents']
    success_url = reverse_lazy('list')

class NPC_DetailView(DetailView):
    model = NPC
    template_name = 'NCID/NPC_detail.html'

class NPC_UpdateView(UpdateView):
    model = NPC
    fields = ['title', 'contents']
    template_name = 'NCID/NPC_update.html'

class NPC_DeleteView(DeleteView):
    model = NPC
    success_url = reverse_lazy('list')
    template_name = 'NCID/NPC_delete.html'

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["repassword"]:
            student_ID = request.POST['student_ID']
            name = request.POST['name']
            password = request.POST['password']
            user = User.objects.create_user(student_ID, name, password)
            auth.login(request, user)
            return redirect('list')
        return redirect('signup')

    return render(request, 'NCID/signup.html')

def login(request):
    if request.method == 'POST':

        student_ID = request.POST["student_ID"]
        password = request.POST["password"]
        user = authenticate(request, username=student_ID, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'NCID/NPC_list.html')
        else:
            return render(request, 'NCID/login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'NCID/login.html')

def logout(request):
    auth.logout(request)
    return redirect('list')

