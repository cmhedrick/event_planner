import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget

from event_planner_app import models


class AddClientForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "First Name"
        }),
        label="First Name"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Last Name"
        }),
        label="Last Name"
    )
    company = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Company"
        }),
        label="Company"
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Phone Number"
        }),
        label="Phone Number"
    )
    e_mail = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': "Email Address"
        }),
        label="Email"
    )

    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)

    def save(self):
        info = self.cleaned_data
        new_client = models.Client.objects.create(
            first_name=info['first_name'],
            last_name=info['last_name'],
            company=info['company'],
            phone_number=info['phone_number'],
            e_mail=info['e_mail'],
        )
        new_client.save()


class AddEventForm(forms.Form):
    event_title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Event Title"
        }),
        label="Event Title"
    )
    event_start_date = forms.DateField(
        widget = SelectDateWidget(
            years = range(
                (
                    datetime.datetime.today() +
                    datetime.timedelta(days=(365 * 5))
                ).year,
                datetime.datetime.now().year
            )
        )
    )
    event_end_date = forms.DateField(
        widget = SelectDateWidget(
            years = range(
                (
                    datetime.datetime.today() +
                    datetime.timedelta(days=(365 * 5))
                ).year,
                datetime.datetime.now().year
            )
        )
    )
    venue_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Venue"
        }),
        label="Venue"
    )
    address_1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Street Name"
        }),
        label="ex: 123 N Hollywoo RD."
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Apt, Suite"
        }),
        label="ex: 100"
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "City"
        }),
        label="City"
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "State"
        }),
        label="State"
    )
    zip = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Zip"
        }),
        label="Zip"
    )
    event_summary = forms.CharField(
        label="Event Summary",
        widget=forms.Textarea(attrs={
            'placeholder': "Event Summary"
        })
    )
    load_in_date = forms.DateField(
        widget = SelectDateWidget(
            years = range(
                (
                    datetime.datetime.today() +
                    datetime.timedelta(days=(365 * 5))
                ).year,
                datetime.datetime.now().year
            )
        )
    )
    load_out_date = forms.DateField(
        widget = SelectDateWidget(
            years = range(
                (
                    datetime.datetime.today() +
                    datetime.timedelta(days=(365 * 5))
                ).year,
                datetime.datetime.now().year
            )
        )
    )
    client = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Client"
        }),
        label="Client"
    )
    truck_parking = forms.CharField(
        label="Truck Parking Instructions",
        widget=forms.Textarea(attrs={
            'placeholder': "Truck Parking Instructions"
        })
    )
    airport = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Airport"
        }),
        label="Airport"
    )
    pm = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': "Project Manager"
        }),
        label="Project Manager"
    )

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)

    def save(self):
        info = self.cleaned_data
        import pdb; pdb.set_trace()
        new_event = models.Event.objects.create(
            first_name=info['first_name'],
            last_name=info['last_name'],
            company=info['company'],
            phone_number=info['phone_number'],
            e_mail=info['e_mail'],
        )
        new_client.save()
