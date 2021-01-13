from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC_bookmark
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.utils import timezone

class Bookmark_ListView(ListView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_list.html'
    paginate_by = 5

    def get_queryset(self):
        return NPC_bookmark.objects.order_by('-time')

def search_bookmark(request):
    blogs = NPC_bookmark.objects.all().order_by('-time')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(url_title__icontains=q)
        return render(request, 'NCID/search_bookmark.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'NCID/search_bookmark.html')

def Bookmark_CreateView(request):
    if request.method == "POST":
        bookmark = NPC_bookmark()
        bookmark.author = request.user.username
        bookmark.url_title = request.POST["url_title"]
        bookmark.url = request.POST["url"]
        bookmark.time = timezone.datetime.now()
        bookmark.save()
        return redirect("bookmark_list")
    return render(request, "NCID/Bookmark_create.html")

class Bookmark_DetailView(DetailView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_detail.html'

def Bookmark_UpdateView(request, pk):
    npc = NPC_bookmark.objects.get(pk=pk)
    if request.method == "POST":
        npc.title = request.POST['title']
        npc.contents = request.POST['contents']
        npc.time = timezone.datetime.now()
        npc.save()
        return redirect('bookmark_list')
    return render(request, 'NCID/Bookmark_update.html', {'npc': npc})

class Bookmark_DeleteView(DeleteView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_delete.html'
    success_url = reverse_lazy('bookmark_list')
