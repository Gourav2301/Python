from django.shortcuts import render
from djando.http import HttpResponse


def hello():
    return HttpResponse('<h1> welcome to billionaire world </h2>')



