from django.db import models

# Create your models here.

SHAPE_CHOICES = (
    ('1', 'Sphere'),
    ('S', 'box'),
    ('R', 'cylinder'),
)

class Shape(models.Model):
    name = models.CharField(max_length=1, choices=SHAPE_CHOICES)
    color = models.IntegerField(max_length=7, help_text='hex')

    def __str__(self):
        return str(self.id)