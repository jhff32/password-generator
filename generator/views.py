from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    characters = list(letters)

    if request.GET.get('uppercase'):
        characters.extend(list(letters.upper()))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
