from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from services.models import Client, Service, TechnicalReport
from inventory.models import Equipment
from quotes.models import Quote
from reports.models import Report
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create users and profiles
        self.stdout.write('Creating users and profiles...')
        admin_user, created = User.objects.get_or_create(username='admin2', defaults={'email': 'admin@personaltech.com'})
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
        admin_profile, _ = Profile.objects.get_or_create(user=admin_user, defaults={'role': 'admin', 'phone': '3001234567', 'company': 'Personal Technology'})

        tech_user, created = User.objects.get_or_create(username='tech1', defaults={'email': 'tech1@personaltech.com'})
        if created:
            tech_user.set_password('tech123')
            tech_user.save()
        tech_profile, _ = Profile.objects.get_or_create(user=tech_user, defaults={'role': 'technician', 'phone': '3002345678', 'company': 'Personal Technology'})

        client_user, created = User.objects.get_or_create(username='client1', defaults={'email': 'client1@example.com'})
        if created:
            client_user.set_password('client123')
            client_user.save()
        client_profile, _ = Profile.objects.get_or_create(user=client_user, defaults={'role': 'client', 'phone': '3003456789', 'company': 'Empresa ABC'})

        # Create clients
        self.stdout.write('Creating clients...')
        client1 = Client.objects.create(
            name='Juan Pérez',
            email='juan@example.com',
            phone='3004567890',
            company='Empresa XYZ',
            address='Calle 123 #45-67, Bogotá',
            type='contract'
        )
        client2 = Client.objects.create(
            name='María García',
            email='maria@example.com',
            phone='3005678901',
            company='Consultoría S.A.',
            address='Carrera 89 #12-34, Medellín',
            type='punctual'
        )
        client3 = Client.objects.create(
            name='Carlos Rodríguez',
            email='carlos@example.com',
            phone='3006789012',
            company='',
            address='Avenida 45 #67-89, Cali',
            type='punctual'
        )

        # Create services
        self.stdout.write('Creating services...')
        service1 = Service.objects.create(
            title='Instalación de servidor',
            description='Instalación y configuración de servidor Dell PowerEdge en oficina principal.',
            client=client1,
            technician=tech_user,
            status='completed'
        )
        service2 = Service.objects.create(
            title='Mantenimiento preventivo',
            description='Revisión y mantenimiento de equipos de cómputo en sucursal norte.',
            client=client2,
            technician=tech_user,
            status='in_progress'
        )
        service3 = Service.objects.create(
            title='Configuración de red',
            description='Configuración de red inalámbrica y firewall.',
            client=client3,
            status='pending'
        )

        # Create technical reports
        self.stdout.write('Creating technical reports...')
        report1 = TechnicalReport.objects.create(
            service=service1,
            technician=tech_user,
            diagnosis='El servidor presentaba fallos en el disco duro principal.',
            interventions='Reemplazo del disco duro defectuoso por uno nuevo. Verificación de backups.',
            parts_used='Disco duro SSD 1TB, Cables SATA',
            recommendations='Implementar monitoreo continuo del estado de los discos.',
            status='final',
            signature='Técnico Juan García'
        )
        report2 = TechnicalReport.objects.create(
            service=service2,
            technician=tech_user,
            diagnosis='Equipos con acumulación de polvo y ventiladores obstruidos.',
            interventions='Limpieza profunda de 15 equipos de escritorio y 5 laptops.',
            parts_used='Aire comprimido, paños antiestáticos',
            recommendations='Establecer calendario de mantenimiento trimestral.',
            status='draft'
        )

        # Create equipment
        self.stdout.write('Creating equipment...')
        eq1 = Equipment.objects.create(
            model='Dell OptiPlex 7090',
            serial_number='DELL123456',
            description='Computador de escritorio para oficina',
            status='available',
            location='Oficina Principal',
            purchase_date=date(2023, 5, 15)
        )
        eq2 = Equipment.objects.create(
            model='HP LaserJet Pro M182nw',
            serial_number='HP789012',
            description='Impresora multifuncional',
            status='in_use',
            location='Sucursal Norte',
            purchase_date=date(2023, 8, 20)
        )
        eq3 = Equipment.objects.create(
            model='Cisco Router 2901',
            serial_number='CISCO345678',
            description='Router para red corporativa',
            status='maintenance',
            location='Data Center',
            purchase_date=date(2022, 12, 10)
        )

        # Create quotes
        self.stdout.write('Creating quotes...')
        quote1 = Quote.objects.create(
            client_name='Ana López',
            client_email='ana@example.com',
            client_phone='3007890123',
            description='Cotización para implementación de sistema de respaldo en la nube.',
            estimated_cost=2500000.00,
            status='sent'
        )
        quote2 = Quote.objects.create(
            client_name='Roberto Martínez',
            client_email='roberto@example.com',
            client_phone='3008901234',
            description='Cotización para migración de servidores legacy.',
            estimated_cost=5000000.00,
            status='accepted'
        )
        quote3 = Quote.objects.create(
            client_name='Sofía Hernández',
            client_email='sofia@example.com',
            client_phone='3009012345',
            description='Cotización para auditoría de seguridad informática.',
            status='pending'
        )

        # Create reports
        self.stdout.write('Creating reports...')
        report_gen1 = Report.objects.create(
            title='Informe de Servicios Completados - Octubre 2025',
            content='Durante octubre se completaron 25 servicios técnicos, con un tiempo promedio de respuesta de 2.5 horas.',
        )
        report_gen2 = Report.objects.create(
            title='Análisis de Inventario - Equipos en Mantenimiento',
            content='Actualmente hay 8 equipos en estado de mantenimiento preventivo.',
        )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))