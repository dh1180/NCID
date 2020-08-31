from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import NPC, NPC_bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Bookmark_ListView(ListView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_list.html'

class Bookmark_CreateView(CreateView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_create.html'
    fields = ['url_title', 'url']
    success_url = reverse_lazy('bookmark_list')

class Bookmark_DetailView(DetailView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_detail.html'

class Bookmark_UpdateView(UpdateView):
    model = NPC_bookmark
    fields = ['url_title', 'url']
    template_name = 'NCID/Bookmark_update.html'

class Bookmark_DeleteView(DeleteView):
    model = NPC_bookmark
    template_name = 'NCID/Bookmark_delete.html'
    success_url = reverse_lazy('bookmark_list')
