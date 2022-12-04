from django.db import models
from django.utils import timezone

from users.models import CustomUser

CATEGORY_CHOICES = (
    ('Легкий', 'Легкий'),
    ('Средний', 'Средний'),
    ('Сложный', 'Сложный'),
)


# модель для категории сложности тура
class Category(models.Model):
    title = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="Легкий")
    slug = models.SlugField()

    def __str__(self):
        return str(self.title)


# модель для видов тура (напр 1-дневный и тд)
class Types(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField()

    def __str__(self):
        return str(self.title)


class Tour(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tours')
    types = models.ForeignKey(Types, on_delete=models.CASCADE, related_name='tours')
    image = models.ImageField()
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField()
    body = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    start_day = models.DateField()
    end_day = models.DateField()
    quantity_of_seats = models.IntegerField()

    def __str__(self):
        return str(self.title)


# Tour.objects.filter(date__range=[date1, date2])

# Модель запись на тур
class Entry(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    date_buy = models.DateField(auto_now_add=True)


# Модель комментарий к туру
class Comment(models.Model):
    image = models.ImageField(blank=True, null=True)
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    user = models.ForeignKey(CustomUser, related_name="comments", verbose_name="Пользователь", default=1,
                             on_delete=models.SET_DEFAULT)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="comments", verbose_name="Тур")

    # def __str__(self):
    #     return f"{self.id}. {self.text}: {self.user.username}"

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Like(models.Model):
    user = models.ForeignKey(CustomUser, related_name='tour_like', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='likes', verbose_name='Тур')

    class Meta:
        unique_together = ['user', 'tour']
