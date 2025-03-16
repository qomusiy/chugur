from django.shortcuts import render

# Create your views here.

def home(r):
    return render(r, template_name='home.html')


def about(r):
    return render(r, template_name='about.html')

def contacts(r):
    return render(r, template_name='contacts.html')
