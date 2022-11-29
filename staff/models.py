from django.db import models


# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=200, )
    staff_email = models.EmailField(unique=True)
