from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ideas/', views.idea_list, name='idea_list'),
    path('ideas/<slug:slug>/', views.idea_detail, name='idea_detail'),
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/<slug:slug>/', views.plan_detail, name='plan_detail'),
]
