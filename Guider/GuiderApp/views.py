from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def guide_view(request):
    return render(request, 'guide.html')

def map1_view(request):
    return render(request, 'map1.html')

def map2_view(request):
    return render(request, 'map2.html')

def tree_view(request):
    return render(request, 'tree.html')

def clothes_view(request):
    return render(request, 'clothes.html')

def achievements_view(request):
    return render(request, 'achievements.html')

def finalmap_view(request):
    return render(request, 'finalmap.html')

def challenges_view(request):
    return render(request, 'challenges.html')
