from django.db import models


class Appointment_Status(models.TextChoices):
    CREATED = ("CREATED", "Created")
    SCHEDULED = ("SCHEDULED", "Scheduled")
    DONE = ("DONE", "Done")
    NOVISIT = ("NOVISIT", "NoVisit")
