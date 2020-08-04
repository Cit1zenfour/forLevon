from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Текст коммента')
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

