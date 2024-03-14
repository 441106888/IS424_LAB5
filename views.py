# person/views.py

from django.shortcuts import render, redirect
from .models import Person

people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)
        return redirect('all_people')
    return render(request, 'person/add.html')

def all_people(request):
    context = {'people': people}
    return render(request, 'person/all.html', context)
