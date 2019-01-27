from django.db import models

class inside_Freeze(models.Model):
    items = models.TextField()
    amount = models.FloatField(default = None) 
    expire_date = models.DateTimeField()
