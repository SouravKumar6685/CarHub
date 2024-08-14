from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mercedes(request):
    return render(request, 'mercedes.html')


def lamborgini(request):
    return render(request, 'lamborgini.html')

def ferrari(request):
    return render(request, 'ferrari.html')


