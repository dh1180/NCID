from django.urls import path
from .views import NCID_ListView, NCID_CreateView, NCID_DetailView, NCID_UpdateView, NCID_DeleteView, grade
from . import views
from .views import signup
from . import views_chat
from .views_bookmark import  Bookmark_CreateView, Bookmark_DeleteView, Bookmark_DetailView, Bookmark_ListView, Bookmark_UpdateView
from django.conf.urls import url

urlpatterns = [
    path('', NCID_ListView.as_view(), name = 'list'),
    path('add/', NCID_CreateView.as_view(), name = 'add'),
    path('detail/<int:pk>/', NCID_DetailView.as_view(), name='detail'),
    path('update/<int:pk>/', NCID_UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NCID_DeleteView.as_view(), name='delete'),

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

    path('grade/', views.grade, name='grade'),


]