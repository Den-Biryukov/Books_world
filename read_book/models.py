from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return f'id - {self.id}: name - {self.name}'