from django.db import models

class Entry(models.Model):
    #Fields
    Inventory_no = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    End_user = models.CharField(max_length = 100)
    Description = models.TextField()
    Brand = models.CharField(max_length = 100)
    Price = models.DecimalField(decimal_places = 0, max_digits = 8)
    Acq_date = models.DateTimeField()
    #Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Inventory'