from django.urls import path
from .views import NCID_ListView,  NCID_DetailView, NCID_UpdateView, NCID_DeleteView, NCID_CreateView, signup
from . import views, views_bookmark, view_crawling, views_university
from .views_bookmark import Bookmark_UpdateView, Bookmark_DeleteView, Bookmark_DetailView, Bookmark_ListView
from .view_crawling import NCID_SchoolMeal_Detail, crawling, NCID_SchoolMeal_List
from .views_university import search, University_ListView, University_DetailView, University_DeleteView
from django.conf.urls import url

urlpatterns = [
    path('', NCID_ListView.as_view(), name = 'list'),
    path('NCID_add/', views.NCID_CreateView, name='NCID_add'),

    path('detail/<int:pk>/', NCID_DetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.NCID_UpdateView, name='update'),
    path('delete/<int:pk>/', views.NCID_DeleteView, name='delete'),

    path('signup/', signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('bookmark/', Bookmark_ListView.as_view(), name='bookmark_list'),
    path('bookmark/detail/<int:pk>/', Bookmark_DetailView.as_view(), name='bookmark_detail'),
    path('bookmark/delete/<int:pk>/', Bookmark_DeleteView.as_view(), name='bookmark_delete'),
    path('bookmark/update/<int:pk>/', views_bookmark.Bookmark_UpdateView, name='bookmark_update'),
    path('bookmark/bookmark_add', views_bookmark.Bookmark_CreateView, name='bookmark_add'),

    path('university/', University_ListView.as_view(), name='university'),
    path('university/detail/<int:pk>', University_DetailView.as_view(), name='university_detail'),
    path('university/university_add', views_university.University_CreateView, name='university_add'),
    path('university/delete/<int:pk>', views_university.University_DeleteView, name='university_delete'),

    path('grade/', views.grade, name='grade'),

    path('search/', views.search, name='search'),
    path('search_bookmark/', views_bookmark.search_bookmark, name='search_bookmark'),
    path('search_meal/', view_crawling.search_meal, name='search_meal'),
    path('search_university/', views_university.search, name='search_university'),

    path('meal/', NCID_SchoolMeal_List.as_view(), name='meal_list'),
    path('meal/create', view_crawling.crawling, name='meal'),
    path('meal/detail/<int:pk>/', NCID_SchoolMeal_Detail.as_view(), name='meal_detail'),


]