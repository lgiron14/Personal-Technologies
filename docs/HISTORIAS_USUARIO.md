# Historias de Usuario - Sistema de Gestión de Servicios Técnicos

## Introducción

Este documento contiene las 34 historias de usuario que dieron origen al desarrollo del sistema de gestión de servicios técnicos para Personal Technology. Las historias están organizadas por roles de usuario y funcionalidades principales del sistema.

## Roles de Usuario

### 1. Administrador
Usuario con acceso completo al sistema para gestionar usuarios, configurar el sistema y generar reportes globales.

### 2. Técnico
Usuario que realiza los servicios técnicos, registra diagnósticos y administra equipos.

### 3. Cliente
Usuario final que solicita servicios, recibe cotizaciones y consulta el estado de sus solicitudes.

## Historias de Usuario por Funcionalidad

### Gestión de Usuarios y Autenticación

**HU-001: Como administrador, quiero poder crear cuentas de usuario para técnicos y clientes**
- **Criterios de aceptación:**
  - Poder crear usuarios con roles específicos (admin, técnico, cliente)
  - Asignar permisos según el rol
  - Enviar notificación de creación de cuenta por email

**HU-002: Como usuario registrado, quiero poder iniciar sesión en el sistema**
- **Criterios de aceptación:**
  - Autenticación segura con email y contraseña
  - Recuperación de contraseña
  - Sesiones persistentes

**HU-003: Como administrador, quiero poder gestionar los roles y permisos de los usuarios**
- **Criterios de aceptación:**
  - Modificar roles de usuarios existentes
  - Desactivar cuentas de usuario
  - Ver historial de actividades por usuario

### Gestión de Clientes

**HU-004: Como administrador, quiero poder registrar nuevos clientes en el sistema**
- **Criterios de aceptación:**
  - Registrar información básica del cliente (nombre, contacto, tipo)
  - Clasificar clientes por tipo (contrato TI o servicio puntual)
  - Asociar cliente con usuario del sistema si aplica

**HU-005: Como técnico, quiero poder consultar la información de los clientes**
- **Criterios de aceptación:**
  - Buscar clientes por nombre, email o NIT
  - Ver historial de servicios realizados
  - Acceder a información de contacto actualizada

**HU-006: Como cliente, quiero poder actualizar mi información de contacto**
- **Criterios de aceptación:**
  - Editar datos personales y de contacto
  - Cambiar contraseña
  - Ver mi historial de servicios

### Gestión de Servicios Técnicos

**HU-007: Como cliente, quiero poder solicitar un servicio técnico**
- **Criterios de aceptación:**
  - Formulario de solicitud con descripción del problema
  - Selección del tipo de servicio requerido
  - Adjuntar archivos relevantes (fotos, documentos)
  - Recibir confirmación de recepción de solicitud

**HU-008: Como técnico, quiero poder registrar un nuevo servicio técnico**
- **Criterios de aceptación:**
  - Crear registro de servicio con cliente asociado
  - Especificar tipo de servicio (revisión, instalación, mantenimiento, etc.)
  - Registrar fecha programada y responsable
  - Actualizar estado del servicio

**HU-009: Como técnico, quiero poder actualizar el estado de un servicio en proceso**
- **Criterios de aceptación:**
  - Cambiar estado (pendiente, en proceso, completado, cancelado)
  - Agregar notas de progreso
  - Registrar tiempo invertido
  - Notificar cambios al cliente

**HU-009.1: Como administrador, quiero poder asignar técnicos a servicios específicos**
- **Criterios de aceptación:**
  - Ver lista de servicios pendientes de asignación
  - Asignar técnico disponible según especialización
  - Reasignar técnico si es necesario
  - Notificar al técnico asignado

### Gestión de Equipos e Inventario

**HU-010: Como administrador, quiero poder gestionar el inventario de equipos**
- **Criterios de aceptación:**
  - Registrar nuevos equipos con número de serie
  - Actualizar estado de equipos (disponible, en uso, mantenimiento, fuera de servicio)
  - Asignar equipos a servicios técnicos
  - Generar reportes de inventario

**HU-011: Como técnico, quiero poder consultar la disponibilidad de equipos**
- **Criterios de aceptación:**
  - Buscar equipos por modelo, marca o estado
  - Ver historial de uso de equipos
  - Reservar equipos para servicios
  - Registrar devolución de equipos

### Gestión de Diagnósticos y Reportes Técnicos

**HU-012: Como técnico, quiero poder crear un diagnóstico técnico**
- **Criterios de aceptación:**
  - Asociar diagnóstico con un servicio específico
  - Registrar hallazgos técnicos detallados
  - Clasificar tipo de problema identificado
  - Recomendar soluciones o repuestos necesarios

**HU-013: Como técnico, quiero poder generar reportes técnicos en PDF**
- **Criterios de aceptación:**
  - Generar reporte con toda la información del servicio
  - Incluir diagnóstico, soluciones aplicadas y recomendaciones
  - Adjuntar fotos o evidencia del trabajo realizado
  - Enviar reporte automáticamente al cliente

**HU-014: Como cliente, quiero poder consultar mis reportes técnicos**
- **Criterios de aceptación:**
  - Ver lista de todos mis servicios realizados
  - Descargar reportes en PDF
  - Ver estado actual de servicios en proceso
  - Contactar al técnico asignado

### Gestión de Cotizaciones

**HU-015: Como cliente, quiero poder solicitar una cotización**
- **Criterios de aceptación:**
  - Formulario de solicitud de cotización
  - Describir el servicio o proyecto requerido
  - Recibir cotización por email
  - Aceptar o rechazar cotización en línea

**HU-016: Como administrador, quiero poder gestionar las cotizaciones**
- **Criterios de aceptación:**
  - Revisar solicitudes de cotización
  - Generar cotizaciones con costos estimados
  - Actualizar estado de cotizaciones
  - Generar reportes de cotizaciones

### Dashboard y Reportes

**HU-017: Como administrador, quiero ver un dashboard con métricas clave**
- **Criterios de aceptación:**
  - Ver número total de servicios por mes
  - Servicios más solicitados
  - Tiempo promedio de respuesta
  - Clientes más activos
  - Estado actual del inventario

**HU-018: Como técnico, quiero ver mi dashboard personal**
- **Criterios de aceptación:**
  - Ver servicios asignados pendientes
  - Servicios completados en el mes
  - Tiempo promedio por servicio
  - Equipos asignados actualmente

**HU-019: Como cliente, quiero ver mi panel de control**
- **Criterios de aceptación:**
  - Ver estado de mis solicitudes activas
  - Historial de servicios realizados
  - Próximas citas programadas
  - Cotizaciones pendientes

### Sistema de Notificaciones

**HU-020: Como sistema, quiero enviar notificaciones automáticas**
- **Criterios de aceptación:**
  - Notificar creación de nuevos servicios
  - Recordatorios de citas programadas
  - Notificaciones de cambio de estado de servicios
  - Alertas de mantenimiento de equipos
  - Envío de reportes por email

### Gestión de Tipos y Categorizaciones

**HU-021: Como administrador, quiero poder gestionar los tipos de servicio**
- **Criterios de aceptación:**
  - Crear, editar y eliminar tipos de servicio (revisión, instalación, mantenimiento, etc.)
  - Asignar precios base por tipo de servicio
  - Configurar tiempos estimados por tipo
  - Activar/desactivar tipos de servicio

**HU-022: Como administrador, quiero poder gestionar los tipos de cliente**
- **Criterios de aceptación:**
  - Definir categorías de cliente (contrato TI, servicio puntual, etc.)
  - Configurar descuentos o precios especiales por tipo
  - Establecer SLA (Service Level Agreement) por tipo de cliente
  - Generar reportes por tipo de cliente

### Gestión de Visitas Técnicas

**HU-023: Como técnico, quiero poder programar visitas técnicas**
- **Criterios de aceptación:**
  - Agendar visitas con fecha y hora específicas
  - Ver disponibilidad de agenda
  - Recibir confirmación de programación
  - Modificar o cancelar visitas programadas

**HU-024: Como cliente, quiero poder ver mi historial de visitas técnicas**
- **Criterios de aceptación:**
  - Ver todas las visitas realizadas ordenadas por fecha
  - Ver detalles de cada visita (técnico, fecha, duración)
  - Descargar reportes de visitas específicas
  - Ver estado de visitas programadas

**HU-025: Como administrador, quiero poder gestionar el calendario de visitas**
- **Criterios de aceptación:**
  - Ver calendario general de todos los técnicos
  - Reprogramar visitas por conflictos
  - Asignar visitas de emergencia
  - Generar reportes de ocupación de técnicos

### Gestión de Productos y Repuestos

**HU-026: Como técnico, quiero poder registrar productos/repuestos utilizados en un servicio**
- **Criterios de aceptación:**
  - Seleccionar productos del inventario
  - Registrar cantidad utilizada
  - Actualizar stock automáticamente
  - Generar lista de materiales por servicio

**HU-027: Como administrador, quiero poder gestionar el catálogo de productos**
- **Criterios de aceptación:**
  - Crear, editar y eliminar productos del catálogo
  - Configurar precios y costos
  - Gestionar proveedores
  - Controlar niveles de stock mínimo

### Firma Digital y Validación

**HU-028: Como técnico, quiero poder firmar digitalmente los reportes técnicos**
- **Criterios de aceptación:**
  - Firmar reportes con certificado digital
  - Verificar integridad del documento firmado
  - Enviar reportes firmados al cliente
  - Mantener registro de firmas por técnico

**HU-029: Como cliente, quiero poder validar la autenticidad de mis reportes**
- **Criterios de aceptación:**
  - Verificar firma digital en reportes
  - Confirmar que el reporte no ha sido alterado
  - Ver información del técnico que firmó
  - Descargar certificado de firma si es necesario

### Gestión de Backup y Recuperación

**HU-030: Como administrador, quiero poder gestionar backups del sistema**
- **Criterios de aceptación:**
  - Configurar backups automáticos programados
  - Realizar backups manuales bajo demanda
  - Restaurar datos desde backups específicos
  - Verificar integridad de backups
  - Almacenar backups en la nube (Azure/AWS)

### Integración con Calendario

**HU-031: Como técnico, quiero sincronizar visitas con mi calendario personal**
- **Criterios de aceptación:**
  - Exportar visitas a Google Calendar/Outlook
  - Recibir recordatorios automáticos
  - Actualizar calendario cuando se reprograman visitas
  - Ver conflictos de agenda

### Reportes Avanzados

**HU-032: Como administrador, quiero generar reportes de rendimiento de técnicos**
- **Criterios de aceptación:**
  - Ver estadísticas por técnico (servicios completados, tiempo promedio, satisfacción del cliente)
  - Comparar rendimiento entre técnicos
  - Identificar áreas de mejora
  - Generar reportes de productividad mensual

**HU-033: Como administrador, quiero generar reportes financieros**
- **Criterios de aceptación:**
  - Reportes de ingresos por servicios
  - Costos de repuestos utilizados
  - Margen de ganancia por tipo de servicio
  - Proyecciones financieras basadas en servicios programados

## Flujo Principal del Sistema

### Proceso de Servicio Técnico Completo

1. **Cliente solicita servicio** (HU-007)
2. **Administrador asigna técnico** (HU-008, HU-009.1)
3. **Técnico programa visita** (HU-023)
4. **Técnico realiza visita y registra diagnóstico** (HU-012, HU-026)
5. **Sistema actualiza estado del servicio** (HU-009)
6. **Técnico genera y firma reporte técnico** (HU-013, HU-028)
7. **Cliente recibe notificación y reporte validado** (HU-014, HU-020, HU-029)
8. **Cliente puede consultar historial de visitas** (HU-024)

### Proceso de Cotización

1. **Cliente solicita cotización** (HU-015)
2. **Administrador revisa y genera cotización** (HU-016)
3. **Cliente recibe y responde a cotización** (HU-015)
4. **Si aceptada, se crea servicio técnico** (HU-007)

## Criterios de Priorización

### Alta Prioridad (Sprint 1-2)
- HU-001, HU-002, HU-003 (Autenticación y gestión de usuarios)
- HU-004, HU-005, HU-006 (Gestión básica de clientes)
- HU-007, HU-008, HU-009, HU-009.1 (Gestión de servicios y asignación)
- HU-021, HU-022 (Tipos de servicio y cliente)
- HU-012, HU-013 (Diagnósticos y reportes)

### Media Prioridad (Sprint 3-4)
- HU-010, HU-011 (Gestión de inventario)
- HU-023, HU-024, HU-025 (Gestión de visitas técnicas)
- HU-015, HU-016 (Sistema de cotizaciones)
- HU-026, HU-027 (Productos y repuestos)
- HU-017, HU-018, HU-019 (Dashboards)

### Baja Prioridad (Sprint 5-6)
- HU-028, HU-029 (Firma digital y validación)
- HU-020 (Sistema de notificaciones avanzado)
- HU-030 (Backup y recuperación)
- HU-031 (Integración con calendario)

### Muy Baja Prioridad (Sprint 7+)
- HU-032, HU-033 (Reportes avanzados y financieros)
- Funcionalidades adicionales de reporting

## Notas Técnicas

- Todas las historias requieren interfaz responsive con Bootstrap 5
- Los reportes técnicos deben generarse en PDF con firma digital
- El sistema debe manejar archivos adjuntos (fotos, documentos, firmas)
- Se requiere integración con PostgreSQL como base de datos principal
- El sistema debe ser desplegable en Azure App Services
- Sistema de backup automático con almacenamiento en la nube
- Integración con calendarios externos (Google Calendar, Outlook)
- API REST completa para futuras integraciones
- Sistema de roles y permisos granular
- Encriptación de datos sensibles y firma digital de documentos