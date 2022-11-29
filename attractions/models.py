from django.db import models

"""Модель достопримечательностей... """


class Attractions(models.Model):
    image = models.ImageField(verbose_name='image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# test