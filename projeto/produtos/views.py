from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Produto

# Create your views here.

def inicio(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html',{'produtos':produtos})
