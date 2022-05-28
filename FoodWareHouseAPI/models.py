from django.db import models

# Create your models here.

class foods(models.Model):
    Mfd_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    unitStock = models.PositiveSmallIntegerField

    def __str__(self):
        return self.Name
