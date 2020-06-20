from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator_files/home.html')

def about(request):
    return render(request, 'generator_files/about.html')
    
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+{}|?><'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length'))
    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator_files/password.html', {'password':thePassword})
