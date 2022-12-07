from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from travel.models import Tour


class OrderCertificate(models.Model):
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tours')
    info = models.TextField()
    count_people = models.PositiveIntegerField(validators=[MaxValueValidator(1)])
    email = models.EmailField()
    phone = PhoneNumberField(null=True, region='KG')
    sender = models.CharField(max_length=50)
    addressee = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tours)
