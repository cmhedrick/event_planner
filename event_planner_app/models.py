from datetime import datetime
from django.db import models


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()
    emergency_contact = models.ForeignKey(EmergencyContact)
    created_date = models.DateTimeField('Created Date', default=datetime.now())


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    start_date = models.DateTimeField('Start Date', default=datetime.now())
    end_date = models.DateTimeField('End Date', default=datetime.now())
    venue_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
