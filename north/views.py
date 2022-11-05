from xml.etree.ElementInclude import include
from django.shortcuts import render
from django.http import HttpResponse
from .models import nculture
from math import ceil
# Create your views here.

def nhome(request):
    products=nculture.objects.all()
    n=len(products)
    nslides=n//4+ceil((n/4)-(n//4))
    params={'nslides':nslides, 'range': range(nslides),'products': products}
    print(params)
    return render(request,"kashmir.html",params)

def productview(request, id):
    product=nculture.objects.filter(id=id)
    return render(request, "pview.html")

