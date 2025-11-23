#!/usr/bin/env python
"""
Script para crear la base de datos PostgreSQL automáticamente.
Ejecutar antes de las migraciones de Django.
"""

import os
import sys
from pathlib import Path

# Agregar el directorio del proyecto al path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_tech.settings')

import django
from django.conf import settings
from decouple import config

django.setup()

def create_database_if_not_exists():
    """
    Crea la base de datos PostgreSQL si no existe.
    """
    try:
        import psycopg2
        from psycopg2 import sql

        # Conectar a PostgreSQL sin especificar base de datos
        conn_params = {
            'host': config('DB_HOST', default='localhost'),
            'port': config('DB_PORT', default='5432'),
            'user': config('DB_USER', default='postgres'),
            'password': config('DB_PASSWORD', default='password'),
        }

        # Conectar a la base de datos 'postgres' por defecto
        conn = psycopg2.connect(**conn_params, database='postgres')
        conn.autocommit = True
        cursor = conn.cursor()

        db_name = config('DB_NAME', default='personal_tech')

        # Verificar si la base de datos existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()

        if not exists:
            # Crear la base de datos
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            print(f"✅ Base de datos '{db_name}' creada exitosamente.")
        else:
            print(f"ℹ️ La base de datos '{db_name}' ya existe.")

        cursor.close()
        conn.close()

    except ImportError:
        print("❌ psycopg2 no está instalado. Instala con: pip install psycopg2-binary")
        return False
    except Exception as e:
        print(f"❌ Error al crear la base de datos: {e}")
        return False

    return True

if __name__ == '__main__':
    print("🔧 Verificando/creando base de datos PostgreSQL...")
    success = create_database_if_not_exists()
    if success:
        print("✅ Proceso completado. Ahora puedes ejecutar 'python manage.py migrate'")
    else:
        print("❌ Falló la creación de la base de datos.")
        sys.exit(1)