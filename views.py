from django.shortcuts import render
from django.http import HttpResponse

def fusion_homepage(request):
    return HttpResponse("Fusion Application Home Page")

def fusion_installation(request):
    return HttpResponse("Install Application")

def fusion_documentation(request):
    return HttpResponse("Fusion Documentation Application")

def custom_page(request):
    return render(request, "admin/custom_page.html")