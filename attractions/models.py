from django.db import models


class Attractions(models.Model):
    """Модель достопримечательностей """
    image = models.ImageField(blank=True, null=True, verbose_name='image', upload_to='attractions_image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
