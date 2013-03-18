import datetime
from django.utils import timezone
from django.db import models
'''
class Integrated_circuit(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
class Manufacturer(models.Model):
    integrated_circuit = models.ForeignKey(Integrated_circuit)
    manufacturer_name = models.CharField(max_length=200)
    contact_number = models.IntegerField(default=0)
    contact_email = models.CharField(max_length=200)
    def __unicode__(self):
        return self.manufacturer_name
'''
# Create your models here.
