from django.urls import path
from .views import NPC_ListView, NPC_CreateView, NPC_DetailView, NPC_UpdateView, NPC_DeleteView
from . import views
from .views import signup
from . import views_chat
from .views_bookmark import  Bookmark_CreateView, Bookmark_DeleteView, Bookmark_DetailView, Bookmark_ListView, Bookmark_UpdateView
from django.conf.urls import url

urlpatterns = [
    path('', NPC_ListView.as_view(), name = 'list'),
    path('add/', NPC_CreateView.as_view(), name = 'add'),
    path('detail/<int:pk>/', NPC_DetailView.as_view(), name='detail'),
    path('update/<int:pk>/', NPC_UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NPC_DeleteView.as_view(), name='delete'),

    path('signup/', signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('bookmark/', Bookmark_ListView.as_view(), name='bookmark_list'),
    path('bookmark/detail/<int:pk>/', Bookmark_DetailView.as_view(), name='bookmark_detail'),
    path('bookmark/delete/<int:pk>/', Bookmark_DeleteView.as_view(), name='bookmark_delete'),
    path('bookmark/update/<int:pk>/', Bookmark_UpdateView.as_view(), name='bookmark_update'),
    path('bookmark/create/', Bookmark_CreateView.as_view(), name='bookmark_create'),

    path('chat/', views_chat.index, name='index'),
    path('chat/<room_name>/', views_chat.room, name='room'),


]