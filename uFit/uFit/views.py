from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def privacyPage(request):
 
    return render(request, 'uFit/privacy.html')