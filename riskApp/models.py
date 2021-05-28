from django.db import models

# Create your models here.

class accountReceivable(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=11)
    probability = models.FloatField()
    dueDate = models.DateTimeField()

