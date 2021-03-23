from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC_university, User
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.utils import timezone


class University_ListView(ListView):
    model = NPC_university
    template_name = 'NCID/University_list.html'
    paginate_by = 5

    def get_queryset(self):
        return NPC_university.objects.order_by('-time')


def search(request):
    blogs = NPC_university.objects.all().order_by('-time')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'NCID/search_university.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'NCID/search_university.html')


def University_CreateView(request):
    if request.method == "POST":
        npc = NPC_university()
        npc.author = request.user.username
        npc.title = request.POST["title"]
        npc.contents = request.POST["contents"]
        npc.time = timezone.datetime.now()
        npc.file = request.FILES['file']
        npc.save()
        return redirect('university')
    return render(request, 'NCID/University_add.html')


class University_DetailView(DetailView):
    model = NPC_university
    template_name = 'NCID/University_detail.html'


def University_UpdateView(request, pk):
    npc = NPC_university.objects.get(pk=pk)
    if request.method == "POST":
        npc.title = request.POST['title']
        npc.contents = request.POST['contents']
        npc.file = request.POST['file']
        npc.time = timezone.datetime.now()
        npc.save()
        return redirect('list')
    return render(request, 'NCID/University_update.html', {'npc': npc})


def University_DeleteView(request, pk):
    ncid = NPC_university.objects.get(pk=pk)
    ncid.delete()
    return redirect('university')