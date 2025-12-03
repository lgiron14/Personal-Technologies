#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script maestro para configurar completamente la base de datos.
Ejecuta en orden:
1. Creación de la base de datos PostgreSQL
2. Migraciones de Django
3. Población de datos de prueba (seeding)
"""

import os
import io
import sys
import subprocess
from pathlib import Path

# Configurar UTF-8 para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Colores para la terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header(message):
    """Imprime un encabezado destacado."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{message}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.ENDC}\n")


def print_success(message):
    """Imprime un mensaje de éxito."""
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")


def print_error(message):
    """Imprime un mensaje de error."""
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")


def print_warning(message):
    """Imprime un mensaje de advertencia."""
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")


def print_info(message):
    """Imprime un mensaje informativo."""
    print(f"{Colors.OKCYAN}ℹ️  {message}{Colors.ENDC}")


def run_command(command, description):
    """
    Ejecuta un comando y maneja errores.
    
    Args:
        command: Lista con el comando y sus argumentos
        description: Descripción de lo que hace el comando
    
    Returns:
        bool: True si el comando fue exitoso, False en caso contrario
    """
    print_info(f"{description}...")
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        if result.stdout:
            print(result.stdout)
        print_success(f"{description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Error en {description}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False
    except Exception as e:
        print_error(f"Error inesperado: {e}")
        return False


def main():
    """Función principal que ejecuta todo el proceso."""
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    print_header("🚀 CONFIGURACIÓN COMPLETA DE BASE DE DATOS")
    print_info(f"Directorio del proyecto: {BASE_DIR}")
    
    # Paso 1: Crear la base de datos
    print_header("PASO 1: Creación de Base de Datos PostgreSQL")
    create_db_script = BASE_DIR / 'scripts' / 'create_database.py'
    if not run_command(
        [sys.executable, str(create_db_script)],
        "Creando base de datos PostgreSQL"
    ):
        print_error("Falló la creación de la base de datos")
        sys.exit(1)
    
    # Paso 2: Ejecutar migraciones
    print_header("PASO 2: Migraciones de Django")
    
    # 2.1: makemigrations
    if not run_command(
        [sys.executable, str(BASE_DIR / 'manage.py'), 'makemigrations'],
        "Generando archivos de migración"
    ):
        print_warning("No se pudieron generar nuevas migraciones (puede ser normal si ya existen)")
    
    # 2.2: migrate
    if not run_command(
        [sys.executable, str(BASE_DIR / 'manage.py'), 'migrate'],
        "Aplicando migraciones a la base de datos"
    ):
        print_error("Falló la aplicación de migraciones")
        sys.exit(1)
    
    # Paso 3: Poblar con datos de prueba
    print_header("PASO 3: Población de Datos de Prueba (Seeding)")
    seed_script = BASE_DIR / 'scripts' / 'seed_database.py'
    if not run_command(
        [sys.executable, str(seed_script)],
        "Poblando base de datos con datos de prueba"
    ):
        print_error("Falló la población de datos")
        sys.exit(1)
    
    # Resumen final
    print_header("✅ CONFIGURACIÓN COMPLETADA EXITOSAMENTE")
    print_success("La base de datos está lista para usar")
    print_info("\n📝 Próximos pasos:")
    print("  1. Ejecuta el servidor: python manage.py runserver")
    print("  2. Accede al admin: http://localhost:8000/admin/")
    print("  3. Usa las credenciales:")
    print("     • Admin: admin1 / admin123")
    print("     • Técnico: tech1 / tech123")
    print("     • Cliente: client1 / client123")
    print(f"\n{Colors.BOLD}¡Listo para desarrollar! 🎉{Colors.ENDC}\n")


if __name__ == '__main__':
    main()
