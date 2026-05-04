import django.db.models as models

class RegistrationStatus(models.TextChoices):
    PENDING = "PEN", "Pending"
    APPROVED = "APP", "Approved"
    REJECTED = "REJ", "Rejected"

class Category(models.TextChoices):
    U_10 = "U_10", "U 10"
    U_11 = "U_11", "U 11"
    U_12 = "U_12", "U 12"
    U_13 = "U_13", "U 13"
    U_14 = "U_14", "U 14"
    U_15 = "U_15", "U 15"
    U_16 = "U_16", "U 16"
    U_17 = "U_17", "U 17"
    U_18 = "U_18", "U 18"
    U_19 = "U_19", "U 19"
    U_20 = "U_20", "U 20"
    U_21 = "U_21", "U 21"
    U_22 = "U_22", "U 22"
    U_23 = "U_23", "U 23"
    SENIOR = "SENIOR", "Senior"
