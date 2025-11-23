from django.contrib import admin
from .models import Client, Service, TechnicalReport

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(TechnicalReport)
