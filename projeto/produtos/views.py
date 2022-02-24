from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Produto

# Create your views here.

def inicio(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html',{'produtos':produtos})

def prodview(request, id):
    prod = get_object_or_404(Produto, pk=id)
    return render(request, 'produto/produto.html', {'prod': prod})