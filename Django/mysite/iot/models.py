from django.db import models

class Event(models.Model):
    #Fields
    node_id = models.CharField(max_length=2)
    node_loc = models.CharField(max_length=10)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)