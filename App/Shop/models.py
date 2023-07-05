from django.db import models


# Create your models here.
class Basket(models.Model):
    Name = models.CharField(max_length=64, default="Basket")
    Total_price = models.IntegerField()



    def __str__(self):
        return f"Basket:{self.id}  Total Price: {self.Total_price}"


class Item(models.Model):
    Name = models.CharField(max_length=64)
    Price = models.DecimalField(decimal_places=2, max_digits=100)
    Description = models.CharField(max_length=5000)
    Basket = models.ManyToManyField(Basket, blank=True, related_name="Items")

    def __str__(self):
        return f"Name: {self.Name} Price: {self.Price} Description: {self.Description}"
