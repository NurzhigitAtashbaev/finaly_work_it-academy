from django.db import models

"""Модель достопримечательностей... """


class Attractions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

