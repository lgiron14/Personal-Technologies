from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('in_use', 'En Uso'),
        ('maintenance', 'En Mantenimiento'),
        ('damaged', 'Dañado'),
    ]
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    location = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.model} - {self.serial_number}'
