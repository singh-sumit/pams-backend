from django.db import models


class User_Role(models.TextChoices):
    ADMIN = ("ADMIN", "Admin")
    RECEPTIONIST = ("RECEPTIONIST", "Receptionist")
    DOCTOR = ("DOCTOR", "Doctor")
    PATIENT = ("PATIENT", "Patient")


class Speciality(models.TextChoices):
    GENERAL = ("GENERAL", "General")
    CARDIOLOGY = ("CARDIOLOGY", "Cardiology")
    NEUROLOGY = ("NEUROLOGY", "Neurology")
    HEMATOLOGY = ("HEMATOLOGY", "Hematology")
    SURGERY = ("SURGERY", "Surgery")
    ORTHOPEDICS = ("ORTHOPEDICS", "Orthopedics")
    PEDIATRICS = ("PEDIATRICS", "Pediatrics")
