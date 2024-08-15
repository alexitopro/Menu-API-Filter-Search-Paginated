from django.db import models

# Create your models here.
class Category(models.Model):
    #slug is a field that is used to create a URL for each category
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    # __str__ is a method that is used to return a string representation of the object
    # str is a built-in Python method that returns a string representation of an object
    def __str__(self)->str:
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    #ForeignKey is used to create a relationship between two models
    #on_delete=models.PROTECT is used to prevent deletion of a category if it has a menu item
    #default=1 is used to set a default category for a menu item
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self)->str:
        return self.title