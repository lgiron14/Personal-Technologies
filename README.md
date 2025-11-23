# Personal Technology - Sistema de Gestión de Servicios TI

## 📋 Descripción

Personal Technology es una aplicación web completa para la gestión de servicios técnicos en el sector de TI.
Desarrollada con Django y Bootstrap 5, ofrece una interfaz moderna y responsiva para administrar clientes, servicios,
reportes técnicos y más.

## 🚀 Características Principales

- **👥 Gestión de Clientes**: Registro y administración de clientes con diferentes tipos (contrato TI o servicio
  puntual)
- **🔧 Gestión de Servicios**: Control completo del ciclo de vida de los servicios técnicos
- **📋 Reportes Técnicos**: Formularios digitalizados para diagnósticos, intervenciones y recomendaciones
- **🎨 Temas Personalizables**: 7 opciones de color para personalizar la interfaz
- **📱 Diseño Responsivo**: Optimizado para dispositivos móviles y desktop
- **🔐 Sistema de Autenticación**: Roles diferenciados (administrador, técnico, cliente)
- **📊 Dashboard**: Panel de control con métricas y estadísticas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Base de Datos**: PostgreSQL (desarrollo: SQLite)
- **Lenguaje**: Python 3.13
- **Estilos**: CSS personalizado con variables CSS

## 📁 Estructura del Proyecto

```
personal_tech/
├── accounts/          # Gestión de usuarios y perfiles
├── services/          # Gestión de servicios y clientes
├── inventory/         # Control de inventario
├── quotes/           # Sistema de cotizaciones
├── reports/          # Reportes y análisis
├── static/           # Archivos estáticos (CSS, JS, imágenes)
├── templates/        # Plantillas HTML
├── docs/             # Documentación del proyecto
│   ├── HISTORIAS_USUARIO.md         # Historias de usuario y requisitos
│   ├── ARQUITECTURA_SOFTWARE.md     # Arquitectura MVC y patrones
│   ├── ARQUITECTURA_BASE_DATOS.md   # Modelo ER y esquemas SQL
│   ├── ARQUITECTURA_INFRAESTRUCTURA.md # Docker, Azure y despliegue
│   └── ARQUITECTURA_FRONTEND.md     # UI/UX y componentes Bootstrap
 │   └── ROLES.md                     # Definición de roles y APIs de gestión
└── personal_tech/    # Configuración principal
```

## 📚 Documentación Técnica

Para una comprensión detallada del sistema, consulta la documentación completa:

- [**📖 Historias de Usuario**](docs/HISTORIAS_USUARIO.md) - Requisitos funcionales y casos de uso del sistema
- [**🏗️ Arquitectura de Software**](docs/ARQUITECTURA_SOFTWARE.md) - Patrón MVC, capas de aplicación, sistema de
  autenticación y roles
- [**🗄️ Arquitectura de Base de Datos**](docs/ARQUITECTURA_BASE_DATOS.md) - Diagrama ER, esquemas SQL, índices y
  optimizaciones
- [**☁️ Arquitectura de Infraestructura**](docs/ARQUITECTURA_INFRAESTRUCTURA.md) - Docker, Azure, CI/CD y monitoreo
- [**🎨 Arquitectura de Frontend**](docs/ARQUITECTURA_FRONTEND.md) - Sistema de diseño, componentes responsive y UX

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8+
- pip
- Virtualenv (recomendado)

### Prerrequisitos Adicionales

- **PostgreSQL**: Instala PostgreSQL en tu sistema
- **Crear base de datos**: Crea una base de datos llamada `personal_tech`

### Instalación

1. **Clona el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd personal_tech
   ```

2. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**

   ```bash
   cp .env.example .env
   # Edita .env con tus configuraciones de PostgreSQL
   ```

5. **Crea la base de datos (opcional, solo para PostgreSQL):**

   ```bash
   python scripts/create_database.py
   # O crea manualmente: CREATE DATABASE personal_tech;
   ```

6. **Configura la base de datos:**

   ```bash
   python manage.py migrate
   ```

7. **Crea un superusuario:**

   ```bash
   python manage.py createsuperuser
   ```

8. **Puebla la base de datos con datos de ejemplo:**

   ```bash
   python manage.py populate_data
   ```

9. **Ejecuta el servidor:**

   ```bash
   python manage.py runserver
   ```

10. **Accede a la aplicación:**
    - URL principal: http://127.0.0.1:8000/
    - Panel de administración: http://127.0.0.1:8000/admin/

## 🎨 Personalización de Temas

La aplicación incluye 7 temas de color que puedes seleccionar desde el menú de usuario:

- 🔵 Azul (predeterminado)
- 🔴 Rojo
- 🟢 Verde
- 🟣 Púrpura
- 🟠 Naranja
- 🔵 Verde Azulado
- ⚫ Oscuro

Los temas se guardan automáticamente en el navegador.

## 📊 Funcionalidades

### Gestión de Clientes

- Crear, editar y eliminar clientes
- Clasificación por tipo (contrato TI / servicio puntual)
- Información de contacto completa

### Gestión de Servicios

- Registro de nuevos servicios
- Asignación de técnicos
- Seguimiento de estados (pendiente, en progreso, completado)
- Historial completo

### Reportes Técnicos

- Formularios digitalizados
- Diagnósticos detallados
- Registro de intervenciones y partes utilizadas
- Recomendaciones técnicas
- Firma digital

### Sistema de Inventario

- Control de equipos y herramientas
- Estados de disponibilidad
- Información de mantenimiento

### Cotizaciones

- Generación de cotizaciones
- Seguimiento de estados
- Estimaciones de costos

## 🔧 Comandos Útiles

```bash
# Ejecutar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Poblar base de datos con datos de ejemplo
python manage.py populate_data

# Ejecutar pruebas
python manage.py test

# Recopilar archivos estáticos
python manage.py collectstatic

# Crear base de datos PostgreSQL automáticamente
python scripts/create_database.py
```

## 🗄️ Gestión de Base de Datos

### Opciones para Crear Base de Datos PostgreSQL

#### 1. **Automática (Recomendada)**

```bash
python scripts/create_database.py
```

#### 2. **Manual con SQL**

```sql
-- Conectar a PostgreSQL como superusuario
psql -U postgres

-- Crear la base de datos
CREATE DATABASE personal_tech;

-- Otorgar permisos al usuario
GRANT ALL PRIVILEGES ON DATABASE personal_tech TO tu_usuario;
```

#### 3. **Con pgAdmin**

1. Abrir pgAdmin
2. Conectar al servidor PostgreSQL
3. Click derecho en "Databases"
4. "Create" > "Database"
5. Nombre: `personal_tech`

#### 4. **Con Docker**

```bash
# Si usas Docker para PostgreSQL
docker run --name postgres-personal-tech \
  -e POSTGRES_DB=personal_tech \
  -e POSTGRES_USER=tu_usuario \
  -e POSTGRES_PASSWORD=tu_password \
  -p 5432:5432 \
  -d postgres:15
```

### Verificación de Conexión

```bash
# Verificar conexión a la base de datos
python manage.py shell -c "from django.db import connection; print('✅ Conectado a:', connection.vendor, connection.settings_dict['NAME'])"
```

## 📝 API REST

La aplicación incluye una API REST desarrollada con Django REST Framework para integraciones externas:

- Endpoints para servicios, clientes y reportes
- Autenticación JWT
- Documentación Swagger/OpenAPI

## 🚀 Despliegue en Producción

### Azure App Services

1. Configura tu aplicación en Azure Portal
2. Configura variables de entorno
3. Despliega usando GitHub Actions o Azure DevOps
4. Configura PostgreSQL en Azure Database

### Docker

```bash
# Construir imagen
docker build -t personal-tech .

# Ejecutar contenedor
docker run -p 8000:8000 personal-tech
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

- **Empresa**: Personal Technology
- **Email**: info@personaltech.com
- **Teléfono**: +57 300 123 4567
- **Dirección**: Medellín, Colombia

## 🙏 Agradecimientos

- Django Framework
- Bootstrap Team
- Comunidad de desarrolladores open source

---

**Desarrollado con ❤️ por Luisa Fernanda Girón**
