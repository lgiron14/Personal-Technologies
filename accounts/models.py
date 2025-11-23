from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('technician', 'Técnico'),
        ('client', 'Cliente'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
