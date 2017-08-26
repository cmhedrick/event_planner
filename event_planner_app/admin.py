from django.contrib import admin

from event_planner_app import models

admin.site.register(models.EmergencyContact)
admin.site.register(models.Employee)
admin.site.register(models.Client)
admin.site.register(models.Event)
