# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    print("HOME")
    return render(request, 'home.html')
