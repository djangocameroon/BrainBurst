from django.shortcuts import render, get_object_or_404
from .models import Idea, Plan

def home(request):
    return render(request, 'builder/home.html')

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'builder/idea_list.html', {'ideas': ideas})

def idea_detail(request, slug):
    idea = get_object_or_404(Idea, slug=slug)
    return render(request, 'builder/idea_detail.html', {'idea': idea})

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'builder/plan_list.html', {'plans': plans})

def plan_detail(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    return render(request, 'builder/plan_detail.html', {'plan': plan})
