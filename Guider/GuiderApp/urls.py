from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guide.html', views.guide_view, name='guide'),
    path('home.html', views.home, name='home'),
    path('map1.html', views.map1_view, name='map1'),
    path('map2.html', views.map2_view, name='map2'),
    path('tree.html', views.tree_view, name='tree'),
    path('clothes.html', views.clothes_view, name='clothes'),
    path('achievements.html', views.achievements_view, name='achievements'),
    path('finalmap.html', views.finalmap_view, name='finalmap'),
    path('challenges.html', views.challenges_view, name='challenges')
]