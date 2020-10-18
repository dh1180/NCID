import requests
from .models import NPC_school
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect

class NCID_SchoolMeal_List(ListView):
    model = NPC_school
    template_name = 'NCID/school_meal.html'
    paginate_by = 5

class NCID_SchoolMeal_Detail(DetailView):
    model = NPC_school
    template_name = 'NCID/school_meal_detail.html'

def search_meal(request):
    blogs = NPC_school.objects.all()

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'NCID/search_meal.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'NCID/search_meal.html')

def crawling(request):
    NPC_school.objects.all().delete()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    url = "https://school.iamservice.net/api/article/organization/10135/group/2015103?next_token=0"

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        json_data = res.json()
        for d in json_data['articles']:
            school = NPC_school()
            school.title = d['title']
            school.contents = d['content']
            school.save()
        return redirect("meal_list")



