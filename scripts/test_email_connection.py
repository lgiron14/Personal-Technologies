import os
import sys
import django
from pathlib import Path

# Setup Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_tech.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email():
    print("Probando configuracion de correo...")
    print(f"   Host: {settings.EMAIL_HOST}")
    print(f"   Port: {settings.EMAIL_PORT}")
    print(f"   User: {settings.EMAIL_HOST_USER}")
    
    try:
        print("\nEnviando correo de prueba...")
        send_mail(
            subject='Prueba de Configuración Personal Tech',
            message='Si estás leyendo esto, la configuración de correo funciona correctamente.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER], # Send to self
            fail_silently=False,
        )
        print("Correo enviado exitosamente!")
        print(f"   Revisa la bandeja de entrada de: {settings.EMAIL_HOST_USER}")
    except Exception as e:
        print("\nError al enviar el correo:")
        print(f"   {str(e)}")

if __name__ == '__main__':
    test_email()
