from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=150, verbose_name='tour_name')
    description = models.TextField(max_length=2000, blank=True, null=True)
    price = models.IntegerField(blank=True,)
    bus = models.ManyToManyField('Bus',)


class Bus(models.Model):
    name = models.CharField(max_length=100,)
    seats_count = models.IntegerField()
