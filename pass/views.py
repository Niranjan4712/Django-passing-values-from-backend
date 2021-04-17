from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    values={'name':'Rohan','age':'24','city':'Kolhapur'}
    return render(request,'home.html',values)