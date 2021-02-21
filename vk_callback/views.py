from django.shortcuts import render
from django.http import HttpResponse


def callback(request):
    print(request)
    return HttpResponse("Hello")
