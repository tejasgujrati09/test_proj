# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Sensor_data
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
	if request.method == 'GET':
		sensor_data = Sensor_data.objects.all()[:10]
		context = {'sensor_data': sensor_data}
		#context = {"data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
		return render(request, 'index.html', context)

	if request.method == 'POST':
	    sensor = request.POST.get("sensor")
	    location = request.POST.get("location")
	    value1 = request.POST.get("value1")
	    value2 = request.POST.get("value2")
	    value3 = request.POST.get("value3")
	    data=Sensor_data(sensor=sensor,location=location,value1=value1,value2=value2,value3=value3)
	    data.save()
	    return HttpResponse("data saved sucessfully")


@csrf_exempt
def save_data(request):
	if request.method == 'GET':	    
	    return HttpResponse("sensor data saved sucessfully")

@csrf_exempt
def about(request):
	return HttpResponse("about")
