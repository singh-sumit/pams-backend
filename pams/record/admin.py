from django.contrib import admin

# Register your models here.
from pams.record.models import Appointment, Record

admin.site.register([Record, Appointment])
