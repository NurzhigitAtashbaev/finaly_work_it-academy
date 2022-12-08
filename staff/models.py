from django.db import models


class AboutStaff(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='staff_images')
    staff_name = models.CharField(max_length=50, )
    professional = models.CharField(max_length=150)
    about = models.TextField(max_length=1000)

    def __str__(self):
        return self.staff_name


class Contacts(models.Model):
    text = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField(blank=True, null=True)
