import django.db.models as models

class RegistrationStatus(models.TextChoices):
    PENDING = "PEN", "Pending"
    APPROVED = "APP", "Approved"
    REJECTED = "REJ", "Rejected"