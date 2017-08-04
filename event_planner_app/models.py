from django.utils import timezone
from django.db import models


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)

class Client(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    company = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()

class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()
    emergency_contact = models.ForeignKey(EmergencyContact)
    created_date = models.DateTimeField('Created Date', default=timezone.now())

class Event(models.Model):
    event_title = models.CharField(max_length=100)
    start_date = models.DateTimeField('Start Date', default=timezone.now())
    end_date = models.DateTimeField('End Date', default=timezone.now())
    load_in = models.DateTimeField('Load In', default=timezone.now())
    load_out = models.DateTimeField('Load Out', default=timezone.now())
    venue_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)

    @property
    def event_location(self):
        return '{0} {1} {2} {3} {4}, {5}'.format(
            self.venue_name,
            self.address_1,
            self.address_2,
            self.city,
            self.state,
            self.zip
        )