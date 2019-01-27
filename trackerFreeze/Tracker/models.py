from django.db import models

class inside_Freeze(models.Model):
    amount = models.FloatField(default = None) 
    items = models.TextField()
    expire_date = models.TextField()
