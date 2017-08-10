from django.db import models


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()
    emergency_contact = models.ForeignKey(
        EmergencyContact, related_name='emergency_contact_for'
    )
    created_date = models.DateTimeField('Created Date', auto_now_add=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Client(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    company = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()

    def __str__(self):
        return self.company


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_start_date = models.DateTimeField(
        'Event Start Date', auto_now_add=True
    )
    event_end_date = models.DateTimeField('Event End Date', auto_now_add=True)
    venue_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=5)
    event_summary = models.TextField()
    load_in = models.DateTimeField('Load In', auto_now_add=True)
    load_out = models.DateTimeField('Load Out', auto_now_add=True)
    client = models.ForeignKey(Client)
    truck_parking = models.TextField()
    airport = models.CharField(max_length=50)
    pm = models.ForeignKey(Employee)

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

    def __str__(self):
        return '{0}: {1} - {2}'.format(
            self.event_title,
            self.load_in,
            self.load_out
        )