from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class CuboidData(models.Model):
    edge_a = models.FloatField()
    edge_b = models.FloatField()
    edge_c = models.FloatField()
    surface_area = models.FloatField()
    volume = models.FloatField()
    perimeter = models.FloatField()
    addedDate = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("addedDate",)
        verbose_name = 'Calculation\'s '
        verbose_name_plural = 'Calculation\'s'

    def __str__(self):
        return str(self.edge_a) + '_' + str(self.edge_b) + str(self.edge_c)


