from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth.models import User



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


class NCID_CreateView(CreateView):
    model = NPC
    template_name = 'NCID/NPC_add.html'
    fields = ['title', 'contents']
    success_url = reverse_lazy('list')

class NCID_DetailView(DetailView):
    model = NPC
    template_name = 'NCID/NPC_detail.html'

class NCID_UpdateView(UpdateView):
    model = NPC
    fields = ['title', 'contents']
    template_name = 'NCID/NPC_update.html'

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

