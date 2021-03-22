# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Sensor_data(models.Model):
    sensor = models.CharField(max_length=30,blank = True)
    location = models.CharField(max_length=30, blank = True)
    value1 = models.CharField(max_length = 15 , blank = True)
    value2 = models.CharField(max_length = 15 , blank = True)
    value3 = models.CharField(max_length = 15 , blank = True)
    reading_time = models.DateTimeField(default=timezone.now())


