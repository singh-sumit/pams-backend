import uuid

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from pams.config.core.db.TimeStampedModel import TimeStampedModel
from pams.config.core.fields.model_fields import LowercaseEmailField
from pams.config.core.validators import validate_alphabet
from pams.users.choice import Speciality
from pams.users.managers import CustomUserManager, DoctorManager, ReceptionistManager


class User(AbstractBaseUser):
    class Meta:
        db_table = "users"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = LowercaseEmailField(unique=True)
    first_name = models.CharField(max_length=50, validators=[validate_alphabet])
    last_name = models.CharField(max_length=50, validators=[validate_alphabet])
    # role = models.CharField(max_length=50, choices=User_Role.choices)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    is_receptionist = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "password",
    ]

    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Receptionist(User):
    class Meta:
        proxy = True

    # override manager
    receptionist = ReceptionistManager()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50, choices=Speciality.choices, default=Speciality.choices[0][0])

    # override manager
    doctor = DoctorManager()

    def __str__(self):
        return self.user.first_name


class Patient(TimeStampedModel):
    class Meta:
        db_table = "patients"

    first_name = models.CharField(max_length=50, validators=[validate_alphabet])
    last_name = models.CharField(max_length=50, validators=[validate_alphabet])
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
