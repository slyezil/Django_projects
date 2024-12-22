from django.shortcuts import render
# from urllib3 import HTTPResponse
from django.http import HttpResponse
from datetime import datetime
def welcome(request):
    return HttpResponse("Welcome to meeting Planner ")

def date(request):
    return HttpResponse("this page was served at" +str(datetime.now()))