from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)


class Advert(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="adverts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="adverts")


class Review(models.Model):
    text = models.TextField()
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1, validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name="reviews")