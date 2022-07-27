from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
import cv2
from pyzbar.pyzbar import decode

# Create your views here.

def list(request):
    all_cars = models.car.objects.all()
    context = {'all_cars' : all_cars}
    return render(request, 'cars/list.html', context=context)

def add(request):
    if(request.POST):
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.car.objects.create(brand=brand, year=year)
        # if user submitted new car --> listhtml
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')
    

def delete(request):

    if(request.POST):
        # Delete the car
        pk = request.POST['pk']
        try:
            models.car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('pk not found')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')

def qr(request):
        

    return render(request, 'cars/qr.html')