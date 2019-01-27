from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('drff ui index')

def generate_factory(request):
    return HttpResponse('generate factory')
