from xml.etree.ElementInclude import include
from django.shortcuts import render
from django.http import HttpResponse
from .models import nculture, order
from math import ceil
# Create your views here.

def nhome(request):
    products=nculture.objects.all()
    n=len(products)
    nslides=n//4+ceil((n/4)-(n//4))
    params={'nslides':nslides, 'range': range(nslides),'products': products}
    # print(params)
    return render(request,"kashmir.html",params)

def productView(request, pid):
    product=nculture.objects.get(pid=pid)
    print(product)
    params={'pp': product}
    return render(request, "product.html",params)

def cart(request, pid):
    product=nculture.objects.get(pid=pid)
    pdata=order()
    pdata.pid=product.pid
    pdata.pname=product.pname
    pdata.price=product.price
    pdata.desc=product.desc
    pdata.category=product.category
    pdata.image=product.image
    pdata.save()
    params={'pp': product}
    return render(request, "cart.html",params)
