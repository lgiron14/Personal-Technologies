# Roles de Usuario

Este documento describe los roles de usuario definidos en el sistema y los permisos asociados.

Roles:

- **Administrador** (`admin`)

  - Acceso completo al sistema.
  - Puede gestionar usuarios (crear, editar roles), ver reportes globales y configurar opciones críticas.

- **Técnico** (`technician`)

  - Usuario que realiza los servicios técnicos.
  - Registra diagnósticos, informes técnicos y administra equipos asignados.

- **Cliente** (`client`)
  - Usuario final que solicita servicios, recibe cotizaciones y revisa el estado de sus solicitudes.

API para gestión de roles (requerido: usuario autenticado con rol `admin`):

- `GET /accounts/api/users/` — Lista usuarios con su rol.
- `PATCH /accounts/api/users/<id>/role/` — Actualiza el rol del usuario. Payload: `{ "role": "technician" }`.

Ejemplo de uso con `curl` (asumiendo sesión autenticada o token apropiado):

```bash
# Listar usuarios
curl -u admin:admin123 http://127.0.0.1:8000/accounts/api/users/

# Cambiar rol a técnico
curl -u admin:admin123 -X PATCH -H "Content-Type: application/json" -d '{"role":"technician"}' http://127.0.0.1:8000/accounts/api/users/3/role/
```

Poblado inicial de datos de ejemplo:

- Usa el comando `python manage.py populate_data` (ya incluido en `services.management.commands.populate_data`) para
  crear usuarios de ejemplo: `admin2`, `tech1` y `client1`.
