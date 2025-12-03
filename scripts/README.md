# 🗄️ Scripts de Base de Datos

Este directorio contiene scripts para configurar y poblar la base de datos del proyecto Personal Tech.

## 📋 Scripts Disponibles

### 1. `setup_database.py` (Recomendado)
**Script maestro que ejecuta todo el proceso automáticamente.**

Ejecuta en orden:
1. ✅ Crea la base de datos PostgreSQL
2. ✅ Ejecuta las migraciones de Django
3. ✅ Puebla la base de datos con datos de prueba

**Uso:**
```bash
python scripts/setup_database.py
```

---

### 2. `create_database.py`
Crea la base de datos PostgreSQL si no existe.

**Uso:**
```bash
python scripts/create_database.py
```

**Requisitos:**
- PostgreSQL instalado y corriendo
- Variables de entorno configuradas en `.env`:
  - `DB_HOST`
  - `DB_PORT`
  - `DB_USER`
  - `DB_PASSWORD`
  - `DB_NAME`

---

### 3. `seed_database.py`
Puebla la base de datos con datos de prueba realistas.

**Uso:**
```bash
python scripts/seed_database.py
```

**Datos creados:**
- **9 Usuarios** (3 por cada rol):
  - 3 Administradores
  - 3 Técnicos
  - 3 Clientes
- **10 Clientes** (empresas y personas)
- **10 Equipos** (laptops, servidores, switches, etc.)
- **10 Servicios** (en diferentes estados)
- **4 Reportes Técnicos** (para servicios completados)
- **10 Cotizaciones** (en diferentes estados)

---

## 🚀 Inicio Rápido

### Configuración Inicial Completa

```bash
# 1. Asegúrate de tener PostgreSQL corriendo
# 2. Configura tu archivo .env con las credenciales de PostgreSQL
# 3. Ejecuta el script maestro
python scripts/setup_database.py
```

### Configuración Manual (Paso a Paso)

```bash
# 1. Crear la base de datos
python scripts/create_database.py

# 2. Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

# 3. Poblar con datos de prueba
python scripts/seed_database.py
```

---

## 👤 Credenciales de Prueba

Después de ejecutar el seeding, puedes usar estas credenciales:

### Administradores
- **Usuario:** `admin1` | **Contraseña:** `admin123`
- **Usuario:** `admin2` | **Contraseña:** `admin123`
- **Usuario:** `admin3` | **Contraseña:** `admin123`

### Técnicos
- **Usuario:** `tech1` | **Contraseña:** `tech123`
- **Usuario:** `tech2` | **Contraseña:** `tech123`
- **Usuario:** `tech3` | **Contraseña:** `tech123`

### Clientes
- **Usuario:** `client1` | **Contraseña:** `client123`
- **Usuario:** `client2` | **Contraseña:** `client123`
- **Usuario:** `client3` | **Contraseña:** `client123`

---

## 🔧 Solución de Problemas

### Error: "psycopg2 no está instalado"
```bash
pip install psycopg2-binary
```

### Error: "No se puede conectar a PostgreSQL"
1. Verifica que PostgreSQL esté corriendo
2. Verifica las credenciales en tu archivo `.env`
3. Asegúrate de que el puerto 5432 esté disponible

### Error: "La base de datos ya existe"
Esto es normal. El script detecta si la base de datos ya existe y continúa.

### Quiero limpiar y empezar de nuevo
```bash
# Opción 1: Eliminar la base de datos desde PostgreSQL
psql -U postgres
DROP DATABASE personal_tech;
\q

# Opción 2: Usar el script de setup nuevamente
python scripts/setup_database.py
```

---

## 📊 Estructura de Datos

### Modelos Poblados

| Modelo | Cantidad | Descripción |
|--------|----------|-------------|
| User | 9 | 3 admins, 3 técnicos, 3 clientes |
| Profile | 9 | Perfiles asociados a usuarios |
| Client | 10 | Clientes empresariales y puntuales |
| Equipment | 10 | Equipos de inventario |
| Service | 10 | Servicios en diferentes estados |
| TechnicalReport | 4 | Reportes para servicios completados |
| Quote | 10 | Cotizaciones en diferentes estados |

---

## 🔄 Actualización de Datos

Si necesitas actualizar los datos de prueba:

1. **Modificar el script:** Edita `seed_database.py`
2. **Limpiar datos existentes:** Opcional, puedes eliminar registros manualmente
3. **Re-ejecutar:** `python scripts/seed_database.py`

El script detecta automáticamente registros duplicados y los omite.

---

## 📝 Notas Importantes

- ⚠️ **No ejecutar en producción:** Estos scripts son solo para desarrollo
- 🔒 **Cambiar contraseñas:** Las contraseñas de prueba son débiles intencionalmente
- 📧 **Emails ficticios:** Los correos electrónicos son de prueba
- 🔄 **Idempotencia:** Los scripts pueden ejecutarse múltiples veces sin duplicar datos

---

## 🆘 Ayuda

Si encuentras problemas:
1. Revisa los logs de PostgreSQL
2. Verifica las variables de entorno en `.env`
3. Asegúrate de tener todas las dependencias instaladas: `pip install -r requirements.txt`

---

**Última actualización:** 2025-11-30
