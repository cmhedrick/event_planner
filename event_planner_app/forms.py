from django import forms

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
