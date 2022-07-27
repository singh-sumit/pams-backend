from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from pams.users.models import Doctor, Patient, Receptionist

admin.site.register([get_user_model(), Receptionist, Doctor, Patient])
