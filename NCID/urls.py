from django.urls import path
from .views import NCID_ListView, create, NCID_DetailView, NCID_UpdateView, NCID_DeleteView, NCID_CreateView, signup
from . import views, views_bookmark, views_chat, view_crawling
from .views_bookmark import  Bookmark_CreateView, Bookmark_DeleteView, Bookmark_DetailView, Bookmark_ListView, Bookmark_UpdateView, bookmark_create
from .view_crawling import NCID_SchoolMeal_Detail, crawling, NCID_SchoolMeal_List
from django.conf.urls import url

urlpatterns = [
    path('', NCID_ListView.as_view(), name = 'list'),
    path('add/', views.create, name = 'add'),
    path('NCID_add/', views.NCID_CreateView, name='NCID_add'),

    path('detail/<int:pk>/', NCID_DetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.NCID_UpdateView, name='update'),
    path('delete/<int:pk>/', NCID_DeleteView.as_view(), name='delete'),

    path('signup/', signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('bookmark/', Bookmark_ListView.as_view(), name='bookmark_list'),
    path('bookmark/detail/<int:pk>/', Bookmark_DetailView.as_view(), name='bookmark_detail'),
    path('bookmark/delete/<int:pk>/', Bookmark_DeleteView.as_view(), name='bookmark_delete'),
    path('bookmark/update/<int:pk>/', Bookmark_UpdateView.as_view(), name='bookmark_update'),
    path('bookmark/create/', views_bookmark.bookmark_create, name='bookmark_create'),
    path('bookmark/bookmark_add', views_bookmark.Bookmark_CreateView, name='bookmark_add'),

    path('chat/', views_chat.index, name='index'),
    path('chat/<room_name>/', views_chat.room, name='room'),

    path('grade/', views.grade, name='grade'),

    path('university/', views.university, name='university'),

    path('search/', views.search, name='search'),
    path('search_bookmark/', views_bookmark.search_bookmark, name='search_bookmark'),
    path('search_meal/', view_crawling.search_meal, name='search_meal'),

    path('meal/', NCID_SchoolMeal_List.as_view(), name='meal_list'),
    path('meal/create', view_crawling.crawling, name='meal'),
    path('meal/detail/<int:pk>/', NCID_SchoolMeal_Detail.as_view(), name='meal_detail'),


]