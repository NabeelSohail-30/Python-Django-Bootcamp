from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
