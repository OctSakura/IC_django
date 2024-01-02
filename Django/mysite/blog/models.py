from django.db import models

# Create your models here.
class Entry(models.Model):
    #Fields
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'

class Model1(models.Model):
    #Fields
    Inventory_no = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    Description = models.TextField()
    Price = models.DecimalField(decimal_places = 0, max_digits = 8)
    Purchase_date = models.DateTimeField()
    Active = models.BooleanField()
    #Methods
    def __str__(self):
        return 'Iventory #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Inventory'