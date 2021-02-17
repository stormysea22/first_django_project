from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return JsonResponse(responseData)

def index(request):
    return redirect("/blog")

def blog(request):
    return HttpResponse("Placeholder for future blog post.")

def new(request):
    return HttpResponse("place holder for new blog form.")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse(f"my number is {num}")

def edit(request, num):
    return HttpResponse(f"place holder to edit {num}")

def destroy(request, num):
    return redirect("/blog")

def bonus(request):
    return JsonResponse({"title": "My First Blog Post", "content": "Lorem, ipsem dolor sit amet consectetur adipisicing elit."})

