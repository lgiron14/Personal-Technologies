#!/usr/bin/env python
"""
Script para poblar la base de datos con datos de prueba.
Ejecutar después de las migraciones de Django.
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Agregar el directorio del proyecto al path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_tech.settings')

import django
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile
from services.models import Client, Service, TechnicalReport
from inventory.models import Equipment
from quotes.models import Quote


def create_users_and_profiles():
    """
    Crea 3 usuarios para cada rol: admin, technician, client.
    """
    print("\n📋 Creando usuarios y perfiles...")
    
    users_data = [
        # Administradores
        {
            'username': 'admin1',
            'email': 'admin1@personaltech.com',
            'first_name': 'Carlos',
            'last_name': 'Rodríguez',
            'password': 'admin123',
            'role': 'admin',
            'phone': '+502 5555-1001',
            'company': 'Personal Tech'
        },
        {
            'username': 'admin2',
            'email': 'admin2@personaltech.com',
            'first_name': 'María',
            'last_name': 'González',
            'password': 'admin123',
            'role': 'admin',
            'phone': '+502 5555-1002',
            'company': 'Personal Tech'
        },
        {
            'username': 'admin3',
            'email': 'admin3@personaltech.com',
            'first_name': 'Roberto',
            'last_name': 'Méndez',
            'password': 'admin123',
            'role': 'admin',
            'phone': '+502 5555-1003',
            'company': 'Personal Tech'
        },
        # Técnicos
        {
            'username': 'tech1',
            'email': 'tech1@personaltech.com',
            'first_name': 'Luis',
            'last_name': 'Hernández',
            'password': 'tech123',
            'role': 'technician',
            'phone': '+502 5555-2001',
            'company': 'Personal Tech'
        },
        {
            'username': 'tech2',
            'email': 'tech2@personaltech.com',
            'first_name': 'Ana',
            'last_name': 'Martínez',
            'password': 'tech123',
            'role': 'technician',
            'phone': '+502 5555-2002',
            'company': 'Personal Tech'
        },
        {
            'username': 'tech3',
            'email': 'tech3@personaltech.com',
            'first_name': 'Jorge',
            'last_name': 'López',
            'password': 'tech123',
            'role': 'technician',
            'phone': '+502 5555-2003',
            'company': 'Personal Tech'
        },
        # Clientes
        {
            'username': 'client1',
            'email': 'client1@empresa.com',
            'first_name': 'Pedro',
            'last_name': 'Ramírez',
            'password': 'client123',
            'role': 'client',
            'phone': '+502 5555-3001',
            'company': 'Empresa ABC'
        },
        {
            'username': 'client2',
            'email': 'client2@empresa.com',
            'first_name': 'Laura',
            'last_name': 'Flores',
            'password': 'client123',
            'role': 'client',
            'phone': '+502 5555-3002',
            'company': 'Corporación XYZ'
        },
        {
            'username': 'client3',
            'email': 'client3@empresa.com',
            'first_name': 'Miguel',
            'last_name': 'Castillo',
            'password': 'client123',
            'role': 'client',
            'phone': '+502 5555-3003',
            'company': 'Comercial 123'
        },
    ]
    
    created_users = {}
    
    for user_data in users_data:
        # Verificar si el usuario ya existe
        if User.objects.filter(username=user_data['username']).exists():
            print(f"  ⚠️  Usuario '{user_data['username']}' ya existe, omitiendo...")
            user = User.objects.get(username=user_data['username'])
            created_users[user_data['role']] = created_users.get(user_data['role'], []) + [user]
            continue
        
        # Crear usuario
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password']
        )
        
        # Crear perfil solo si no existe
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(
                user=user,
                role=user_data['role'],
                phone=user_data['phone'],
                company=user_data['company']
            )
        
        created_users[user_data['role']] = created_users.get(user_data['role'], []) + [user]
        print(f"  ✅ Usuario '{user_data['username']}' creado con rol '{user_data['role']}'")
    
    return created_users


def create_clients():
    """
    Crea 10 clientes de prueba.
    """
    print("\n👥 Creando clientes...")
    
    clients_data = [
        {
            'name': 'Empresa Tecnológica S.A.',
            'email': 'contacto@emptech.com',
            'phone': '+502 2222-1001',
            'company': 'Empresa Tecnológica S.A.',
            'address': 'Zona 10, Ciudad de Guatemala',
            'type': 'contract'
        },
        {
            'name': 'Comercial Los Alpes',
            'email': 'info@losalpes.com',
            'phone': '+502 2222-1002',
            'company': 'Comercial Los Alpes',
            'address': 'Zona 1, Guatemala',
            'type': 'contract'
        },
        {
            'name': 'Distribuidora Central',
            'email': 'ventas@distcentral.com',
            'phone': '+502 2222-1003',
            'company': 'Distribuidora Central',
            'address': 'Zona 4, Mixco',
            'type': 'contract'
        },
        {
            'name': 'Juan Pérez',
            'email': 'juan.perez@gmail.com',
            'phone': '+502 5555-4001',
            'company': '',
            'address': 'Zona 11, Guatemala',
            'type': 'punctual'
        },
        {
            'name': 'Sofía Morales',
            'email': 'sofia.morales@hotmail.com',
            'phone': '+502 5555-4002',
            'company': '',
            'address': 'Zona 7, Guatemala',
            'type': 'punctual'
        },
        {
            'name': 'Restaurante El Buen Sabor',
            'email': 'admin@buensabor.com',
            'phone': '+502 2222-1004',
            'company': 'Restaurante El Buen Sabor',
            'address': 'Zona 9, Guatemala',
            'type': 'punctual'
        },
        {
            'name': 'Clínica Médica San Rafael',
            'email': 'info@sanrafael.com',
            'phone': '+502 2222-1005',
            'company': 'Clínica Médica San Rafael',
            'address': 'Zona 14, Guatemala',
            'type': 'contract'
        },
        {
            'name': 'Andrea Vásquez',
            'email': 'andrea.v@yahoo.com',
            'phone': '+502 5555-4003',
            'company': '',
            'address': 'Zona 15, Guatemala',
            'type': 'punctual'
        },
        {
            'name': 'Bufete Jurídico Asociados',
            'email': 'contacto@bufetejuridico.com',
            'phone': '+502 2222-1006',
            'company': 'Bufete Jurídico Asociados',
            'address': 'Zona 10, Guatemala',
            'type': 'contract'
        },
        {
            'name': 'Carlos Gómez',
            'email': 'carlos.gomez@outlook.com',
            'phone': '+502 5555-4004',
            'company': '',
            'address': 'Zona 12, Guatemala',
            'type': 'punctual'
        },
    ]
    
    created_clients = []
    
    for client_data in clients_data:
        # Verificar si el cliente ya existe
        if Client.objects.filter(email=client_data['email']).exists():
            print(f"  ⚠️  Cliente '{client_data['name']}' ya existe, omitiendo...")
            client = Client.objects.get(email=client_data['email'])
            created_clients.append(client)
            continue
        
        client = Client.objects.create(**client_data)
        created_clients.append(client)
        print(f"  ✅ Cliente '{client_data['name']}' creado")
    
    return created_clients


def create_equipment():
    """
    Crea 10 equipos de prueba.
    """
    print("\n💻 Creando equipos...")
    
    equipment_data = [
        {
            'model': 'Dell Latitude 5520',
            'serial_number': 'DL5520-001',
            'description': 'Laptop empresarial con procesador Intel i7',
            'status': 'available',
            'location': 'Bodega Principal',
            'purchase_date': datetime.now().date() - timedelta(days=365)
        },
        {
            'model': 'HP ProDesk 400 G7',
            'serial_number': 'HP400-002',
            'description': 'Desktop para oficina',
            'status': 'in_use',
            'location': 'Oficina Técnicos',
            'purchase_date': datetime.now().date() - timedelta(days=180)
        },
        {
            'model': 'Lenovo ThinkPad T14',
            'serial_number': 'LT14-003',
            'description': 'Laptop para técnicos de campo',
            'status': 'in_use',
            'location': 'Asignado a Técnico',
            'purchase_date': datetime.now().date() - timedelta(days=90)
        },
        {
            'model': 'Cisco Catalyst 2960',
            'serial_number': 'CC2960-004',
            'description': 'Switch de red 24 puertos',
            'status': 'available',
            'location': 'Bodega Principal',
            'purchase_date': datetime.now().date() - timedelta(days=730)
        },
        {
            'model': 'Dell PowerEdge R740',
            'serial_number': 'DPE740-005',
            'description': 'Servidor rack 2U',
            'status': 'maintenance',
            'location': 'Centro de Datos',
            'purchase_date': datetime.now().date() - timedelta(days=1095)
        },
        {
            'model': 'HP LaserJet Pro M404dn',
            'serial_number': 'HPL404-006',
            'description': 'Impresora láser monocromática',
            'status': 'available',
            'location': 'Bodega Principal',
            'purchase_date': datetime.now().date() - timedelta(days=200)
        },
        {
            'model': 'APC Smart-UPS 1500VA',
            'serial_number': 'APC1500-007',
            'description': 'UPS para protección de equipos',
            'status': 'in_use',
            'location': 'Sala de Servidores',
            'purchase_date': datetime.now().date() - timedelta(days=500)
        },
        {
            'model': 'Asus ROG Strix G15',
            'serial_number': 'AROG15-008',
            'description': 'Laptop de alto rendimiento',
            'status': 'damaged',
            'location': 'Taller de Reparación',
            'purchase_date': datetime.now().date() - timedelta(days=150)
        },
        {
            'model': 'Synology DS920+',
            'serial_number': 'SYN920-009',
            'description': 'NAS 4 bahías para almacenamiento',
            'status': 'in_use',
            'location': 'Oficina Principal',
            'purchase_date': datetime.now().date() - timedelta(days=300)
        },
        {
            'model': 'Ubiquiti UniFi AP AC Pro',
            'serial_number': 'UAP-010',
            'description': 'Punto de acceso WiFi empresarial',
            'status': 'available',
            'location': 'Bodega Principal',
            'purchase_date': datetime.now().date() - timedelta(days=400)
        },
    ]
    
    created_equipment = []
    
    for equip_data in equipment_data:
        # Verificar si el equipo ya existe
        if Equipment.objects.filter(serial_number=equip_data['serial_number']).exists():
            print(f"  ⚠️  Equipo '{equip_data['model']}' ya existe, omitiendo...")
            equipment = Equipment.objects.get(serial_number=equip_data['serial_number'])
            created_equipment.append(equipment)
            continue
        
        equipment = Equipment.objects.create(**equip_data)
        created_equipment.append(equipment)
        print(f"  ✅ Equipo '{equip_data['model']}' creado")
    
    return created_equipment


def create_services(clients, technicians):
    """
    Crea 10 servicios de prueba.
    """
    print("\n🔧 Creando servicios...")
    
    services_data = [
        {
            'title': 'Instalación de red empresarial',
            'description': 'Instalación completa de red LAN con cableado estructurado categoría 6',
            'status': 'completed'
        },
        {
            'title': 'Mantenimiento preventivo de servidores',
            'description': 'Revisión y limpieza de servidores Dell PowerEdge',
            'status': 'completed'
        },
        {
            'title': 'Reparación de laptop HP',
            'description': 'Laptop no enciende, posible problema en fuente de poder',
            'status': 'in_progress'
        },
        {
            'title': 'Configuración de firewall',
            'description': 'Configuración de reglas de firewall para seguridad de red',
            'status': 'in_progress'
        },
        {
            'title': 'Migración de datos a nuevo servidor',
            'description': 'Migración de base de datos y archivos a servidor nuevo',
            'status': 'pending'
        },
        {
            'title': 'Instalación de sistema de videovigilancia',
            'description': 'Instalación de 8 cámaras IP con grabación en NVR',
            'status': 'pending'
        },
        {
            'title': 'Soporte técnico remoto',
            'description': 'Problemas con correo electrónico en Outlook',
            'status': 'completed'
        },
        {
            'title': 'Actualización de sistema operativo',
            'description': 'Actualización de Windows 10 a Windows 11 en 15 equipos',
            'status': 'in_progress'
        },
        {
            'title': 'Reparación de impresora',
            'description': 'Impresora HP con atasco de papel recurrente',
            'status': 'cancelled'
        },
        {
            'title': 'Instalación de punto de acceso WiFi',
            'description': 'Instalación y configuración de AP Ubiquiti',
            'status': 'completed'
        },
    ]
    
    created_services = []
    
    for i, service_data in enumerate(services_data):
        # Asignar cliente y técnico de forma rotativa
        client = clients[i % len(clients)]
        technician = technicians[i % len(technicians)] if service_data['status'] != 'pending' else None
        
        service = Service.objects.create(
            title=service_data['title'],
            description=service_data['description'],
            client=client,
            technician=technician,
            status=service_data['status']
        )
        created_services.append(service)
        print(f"  ✅ Servicio '{service_data['title']}' creado")
    
    return created_services


def create_technical_reports(services, technicians):
    """
    Crea reportes técnicos para servicios completados.
    """
    print("\n📄 Creando reportes técnicos...")
    
    reports_data = [
        {
            'diagnosis': 'Red empresarial sin infraestructura adecuada. Cableado antiguo categoría 5e.',
            'interventions': 'Instalación de cableado estructurado Cat6, configuración de switch principal, pruebas de conectividad.',
            'parts_used': '50m cable Cat6, 12 conectores RJ45, 1 patch panel 24 puertos',
            'recommendations': 'Realizar mantenimiento anual del cableado. Considerar actualización a Cat6a en el futuro.',
            'warranty_period': '1 año',
            'signature': 'Carlos Rodríguez'
        },
        {
            'diagnosis': 'Servidores con acumulación de polvo y temperatura elevada.',
            'interventions': 'Limpieza profunda de componentes, reemplazo de pasta térmica, verificación de ventiladores.',
            'parts_used': 'Pasta térmica Arctic MX-4',
            'recommendations': 'Programar mantenimiento preventivo cada 6 meses.',
            'warranty_period': '3 meses',
            'signature': 'María González'
        },
        {
            'diagnosis': 'Problema de conectividad intermitente en correo electrónico.',
            'interventions': 'Reconfiguración de perfil de Outlook, actualización de certificados SSL.',
            'parts_used': '',
            'recommendations': 'Mantener Outlook actualizado.',
            'warranty_period': '1 mes',
            'signature': 'Luis Hernández'
        },
        {
            'diagnosis': 'Cobertura WiFi deficiente en área de trabajo.',
            'interventions': 'Instalación de AP Ubiquiti, configuración de SSID y seguridad WPA3.',
            'parts_used': '1 Ubiquiti UniFi AP AC Pro, 30m cable UTP',
            'recommendations': 'Monitorear cobertura con aplicación UniFi.',
            'warranty_period': '2 años',
            'signature': 'Ana Martínez'
        },
    ]
    
    # Crear reportes solo para servicios completados
    completed_services = [s for s in services if s.status == 'completed']
    
    created_reports = []
    
    for i, service in enumerate(completed_services[:len(reports_data)]):
        # Verificar si ya existe un reporte para este servicio
        if TechnicalReport.objects.filter(service=service).exists():
            print(f"  ⚠️  Reporte para '{service.title}' ya existe, omitiendo...")
            continue
        
        report_data = reports_data[i]
        technician = service.technician or technicians[i % len(technicians)]
        
        report = TechnicalReport.objects.create(
            service=service,
            technician=technician,
            diagnosis=report_data['diagnosis'],
            interventions=report_data['interventions'],
            parts_used=report_data['parts_used'],
            recommendations=report_data['recommendations'],
            status='final',
            signature=report_data['signature'],
            warranty_period=report_data['warranty_period']
        )
        created_reports.append(report)
        print(f"  ✅ Reporte técnico para '{service.title}' creado")
    
    return created_reports


def create_quotes():
    """
    Crea 10 cotizaciones de prueba.
    """
    print("\n💰 Creando cotizaciones...")
    
    quotes_data = [
        {
            'client_name': 'Empresa Constructora ABC',
            'client_email': 'info@constructoraabc.com',
            'client_phone': '+502 2222-5001',
            'description': 'Instalación de red completa para oficinas nuevas (50 puntos de red)',
            'estimated_cost': Decimal('15000.00'),
            'status': 'sent'
        },
        {
            'client_name': 'Farmacia La Salud',
            'client_email': 'contacto@farmaciasalud.com',
            'client_phone': '+502 2222-5002',
            'description': 'Sistema de punto de venta con 3 terminales',
            'estimated_cost': Decimal('8500.00'),
            'status': 'accepted'
        },
        {
            'client_name': 'Roberto Díaz',
            'client_email': 'roberto.diaz@gmail.com',
            'client_phone': '+502 5555-5001',
            'description': 'Reparación de computadora de escritorio',
            'estimated_cost': Decimal('350.00'),
            'status': 'pending'
        },
        {
            'client_name': 'Colegio San José',
            'client_email': 'admin@colegiosanjose.edu',
            'client_phone': '+502 2222-5003',
            'description': 'Instalación de laboratorio de computación (20 equipos)',
            'estimated_cost': Decimal('45000.00'),
            'status': 'sent'
        },
        {
            'client_name': 'Panadería El Trigo',
            'client_email': 'ventas@panaderiaeltrigo.com',
            'client_phone': '+502 2222-5004',
            'description': 'Sistema de cámaras de seguridad (6 cámaras)',
            'estimated_cost': Decimal('5500.00'),
            'status': 'accepted'
        },
        {
            'client_name': 'Gabriela Ortiz',
            'client_email': 'gaby.ortiz@hotmail.com',
            'client_phone': '+502 5555-5002',
            'description': 'Configuración de red WiFi en casa',
            'estimated_cost': Decimal('450.00'),
            'status': 'rejected'
        },
        {
            'client_name': 'Hotel Vista Hermosa',
            'client_email': 'reservas@hotelvistahermosa.com',
            'client_phone': '+502 2222-5005',
            'description': 'Actualización de sistema de reservas y WiFi para huéspedes',
            'estimated_cost': Decimal('12000.00'),
            'status': 'pending'
        },
        {
            'client_name': 'Taller Mecánico El Rápido',
            'client_email': 'info@tallerelrapido.com',
            'client_phone': '+502 2222-5006',
            'description': 'Sistema de gestión de inventario de repuestos',
            'estimated_cost': Decimal('6500.00'),
            'status': 'sent'
        },
        {
            'client_name': 'Daniela Ruiz',
            'client_email': 'daniela.ruiz@yahoo.com',
            'client_phone': '+502 5555-5003',
            'description': 'Instalación de impresora en red',
            'estimated_cost': Decimal('250.00'),
            'status': 'accepted'
        },
        {
            'client_name': 'Gimnasio FitZone',
            'client_email': 'contacto@fitzone.com',
            'client_phone': '+502 2222-5007',
            'description': 'Sistema de control de acceso con tarjetas RFID',
            'estimated_cost': Decimal('8000.00'),
            'status': 'pending'
        },
    ]
    
    created_quotes = []
    
    for quote_data in quotes_data:
        # Verificar si la cotización ya existe
        if Quote.objects.filter(client_email=quote_data['client_email'], 
                               description=quote_data['description']).exists():
            print(f"  ⚠️  Cotización para '{quote_data['client_name']}' ya existe, omitiendo...")
            continue
        
        quote = Quote.objects.create(**quote_data)
        created_quotes.append(quote)
        print(f"  ✅ Cotización para '{quote_data['client_name']}' creada")
    
    return created_quotes


def main():
    """
    Función principal que ejecuta todo el proceso de seeding.
    """
    print("=" * 70)
    print("🌱 INICIANDO PROCESO DE SEEDING DE BASE DE DATOS")
    print("=" * 70)
    
    try:
        # 1. Crear usuarios y perfiles
        users = create_users_and_profiles()
        technicians = users.get('technician', [])
        
        # 2. Crear clientes
        clients = create_clients()
        
        # 3. Crear equipos
        equipment = create_equipment()
        
        # 4. Crear servicios
        services = create_services(clients, technicians)
        
        # 5. Crear reportes técnicos
        reports = create_technical_reports(services, technicians)
        
        # 6. Crear cotizaciones
        quotes = create_quotes()
        
        # Resumen
        print("\n" + "=" * 70)
        print("✅ PROCESO DE SEEDING COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        print(f"\n📊 Resumen de datos creados:")
        print(f"  • Usuarios: {User.objects.count()}")
        print(f"  • Perfiles: {Profile.objects.count()}")
        print(f"  • Clientes: {Client.objects.count()}")
        print(f"  • Equipos: {Equipment.objects.count()}")
        print(f"  • Servicios: {Service.objects.count()}")
        print(f"  • Reportes Técnicos: {TechnicalReport.objects.count()}")
        print(f"  • Cotizaciones: {Quote.objects.count()}")
        print("\n💡 Credenciales de acceso:")
        print("  • Admins: admin1/admin123, admin2/admin123, admin3/admin123")
        print("  • Técnicos: tech1/tech123, tech2/tech123, tech3/tech123")
        print("  • Clientes: client1/client123, client2/client123, client3/client123")
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error durante el proceso de seeding: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
