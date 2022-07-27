from django.db import models

# Create your models here.
from pams.record.choice import Appointment_Status
from pams.users.models import Doctor, Patient, Receptionist


class Appointment(models.Model):
    class Meta:
        db_table = "appointments"

    choosed_date = models.DateField(auto_now_add=True, editable=False)
    scheduled_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=Appointment_Status.choices, default=Appointment_Status.choices[0][0]
    )
    scheduled_by = models.ForeignKey(Receptionist, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"ApId--{self.id} // P-{self.patient.first_name} / R-{self.scheduled_by.first_name}"


class Record(models.Model):
    class Meta:
        db_table = "records"

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    prescription = models.TextField()
