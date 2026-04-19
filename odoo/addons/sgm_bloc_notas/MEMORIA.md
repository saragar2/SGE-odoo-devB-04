# Memoria del Módulo SGM Bloc de Notas

**Autor:** Sara García Miguel  
**Fecha:** Febrero 2026  
**Versión:** 0.1  

---

## Índice

1. [Diagrama de Clases UML](#1-diagrama-de-clases-uml)
2. [Finalidad y Funcionamiento del Módulo](#2-finalidad-y-funcionamiento-del-módulo)
3. [Conclusiones Personales](#3-conclusiones-personales)
4. [Problemas Encontrados](#4-problemas-encontrados)
5. [Sugerencias de Mejora](#5-sugerencias-de-mejora)
6. [Referencias Bibliográficas](#6-referencias-bibliográficas)

---

## 1. Diagrama de Clases UML

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                    DIAGRAMA DE CLASES                                    │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────┐       ┌─────────────────────────┐
│   SharedNoteCategory    │       │      SharedNoteTag      │
│  (shared.note.category) │       │    (shared.note.tag)    │
├─────────────────────────┤       ├─────────────────────────┤
│ - name: Char [required] │       │ - name: Char [required] │
│ - description: Text     │       │ - color: Integer        │
│ - note_ids: One2many    │       │ - note_ids: Many2many   │
└───────────┬─────────────┘       └───────────┬─────────────┘
            │                                 │
            │ 1                               │ *
            │                                 │
            ▼ *                               ▼ *
┌─────────────────────────────────────────────────────────────┐
│                        SharedNote                            │
│                      (shared.note)                           │
├─────────────────────────────────────────────────────────────┤
│ - name: Char [required]                                      │
│ - content: Html                                              │
│ - image: Image                                               │
│ - owner_id: Many2one → res.users [required]                  │
│ - category_id: Many2one → shared.note.category               │
│ - tag_ids: Many2many → shared.note.tag                       │
│ - line_ids: One2many → shared.note.line                      │
│ - is_public: Boolean                                         │
│ - last_update: Datetime [computed]                           │
├─────────────────────────────────────────────────────────────┤
│ + _compute_last_update()                                     │
│ + _check_name_not_empty()                                    │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            │ 1
                            │
                            ▼ *
              ┌─────────────────────────────┐
              │      SharedNoteLine         │
              │    (shared.note.line)       │
              ├─────────────────────────────┤
              │ - note_id: Many2one → note  │
              │   [required, cascade]       │
              │ - title: Char [required]    │
              │ - description: Text         │
              │ - done: Boolean             │
              └─────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                    RELACIONES                                            │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│  SharedNoteCategory  ──(1:N)──►  SharedNote      │ Una categoría tiene muchas notas     │
│  SharedNote          ──(N:1)──►  res.users       │ Una nota tiene un propietario        │
│  SharedNote          ──(N:M)──►  SharedNoteTag   │ Notas y etiquetas (muchos a muchos)  │
│  SharedNote          ──(1:N)──►  SharedNoteLine  │ Una nota tiene muchas líneas         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### Descripción de las Clases

| Clase | Descripción |
|-------|-------------|
| **SharedNote** | Modelo principal que representa una nota compartida. Hereda de `mail.thread` y `mail.activity.mixin` para soporte de mensajería. |
| **SharedNoteLine** | Líneas o ítems dentro de una nota (tipo lista de tareas). |
| **SharedNoteCategory** | Categorías para organizar las notas. |
| **SharedNoteTag** | Etiquetas para clasificar las notas con colores. |

---

## 2. Finalidad y Funcionamiento del Módulo

### 2.1 Finalidad

El módulo **SGM Bloc de Notas** es una aplicación para Odoo 17 que permite a los usuarios crear, organizar y compartir notas de forma sencilla. Está diseñado para entornos empresariales donde se necesita gestionar información de manera colaborativa.

### 2.2 Funcionalidades Principales

1. **Gestión de Notas**
   - Crear notas con título, contenido HTML e imagen representativa
   - Marcar notas como públicas o privadas
   - Seguimiento automático de la última actualización

2. **Organización**
   - Clasificar notas por categorías (Personal, Trabajo, Estudios, etc.)
   - Etiquetar notas con múltiples tags de colores
   - Crear listas de tareas dentro de cada nota (líneas)

3. **Colaboración**
   - Sistema de mensajería integrado (chatter)
   - Seguimiento de actividades
   - Asignación de propietario a cada nota

4. **Seguridad**
   - Permisos diferenciados para usuarios internos (sin borrar)
   - Permisos completos para administradores

### 2.3 Estructura de Menús

```
Notas compartidas (menú raíz)
├── Notas          → Lista y formulario de notas
├── Categorías     → Gestión de categorías
└── Etiquetas      → Gestión de tags
```

### 2.4 Flujo de Uso

1. El usuario accede al menú "Notas compartidas"
2. Crea categorías y etiquetas para organizar sus notas
3. Crea una nueva nota asignando categoría, etiquetas e imagen
4. Añade líneas (tareas) a la nota
5. Marca las tareas como completadas según avanza
6. Opcionalmente comparte la nota marcándola como pública

---

## 3. Conclusiones Personales

### Aspectos Positivos

- **Framework robusto**: Odoo proporciona una estructura sólida para el desarrollo de módulos empresariales, con ORM potente y sistema de vistas declarativo.

- **Reutilización de código**: La herencia de mixins como `mail.thread` permite añadir funcionalidades complejas (mensajería, actividades) con mínimo esfuerzo.

- **Desarrollo rápido**: Una vez comprendida la arquitectura MVC de Odoo, el desarrollo de nuevos modelos y vistas es relativamente ágil.

- **Datos demo**: El sistema de datos de demostración facilita las pruebas y la presentación del módulo.

### Aprendizajes

- Comprensión profunda de las relaciones entre modelos (One2many, Many2one, Many2many)
- Uso de campos computados y restricciones (constraints)
- Diseño de vistas XML con elementos anidados
- Gestión de permisos y seguridad en Odoo

---

## 4. Problemas Encontrados

### 4.1 Vistas Anidadas para Many2many

**Problema**: El test requería una vista `<tree>` anidada dentro de los campos Many2many, pero el widget `many2many_tags` oculta visualmente esta estructura.

**Solución**: Añadir la vista tree dentro del campo aunque el widget la sobreescriba visualmente:
```xml
<field name="tag_ids" widget="many2many_tags">
    <tree>
        <field name="name"/>
    </tree>
</field>
```

### 4.2 Propietario por Defecto (OdooBot)

**Problema**: Al cargar datos demo, el campo `owner_id` tomaba el usuario del sistema (OdooBot) en lugar de un usuario real.

**Causa**: El valor `default=lambda self: self.env.user` se evalúa durante la carga de datos, cuando el usuario es OdooBot.

**Solución**: Se puede especificar explícitamente el usuario en el demo.xml o aceptar este comportamiento por defecto.

### 4.3 Código Comentado

**Problema**: Los ficheros generados por scaffold (`models.py`, `controllers.py`, `views.xml`, `templates.xml`) contenían código de ejemplo comentado que hacía fallar los tests de calidad.

**Solución**: Limpiar todos los ficheros eliminando el código comentado y dejando solo la estructura mínima necesaria.

### 4.4 Permisos Diferenciados

**Problema**: Inicialmente todos los usuarios tenían permisos CRUD completos.

**Solución**: Crear dos líneas de permisos por modelo:
- `base.group_user`: Leer, Escribir, Crear (sin Borrar)
- `base.group_system`: CRUD completo

---

## 5. Sugerencias de Mejora

### 5.1 Funcionalidades Adicionales

- **Compartir con usuarios específicos**: Implementar un campo Many2many con `res.users` para seleccionar con quién compartir cada nota.

- **Recordatorios**: Integrar con el sistema de actividades de Odoo para programar recordatorios sobre notas.

- **Búsqueda avanzada**: Añadir filtros y agrupaciones predefinidas (por categoría, por propietario, notas públicas/privadas).

- **Vista Kanban**: Implementar una vista Kanban para visualizar las notas como tarjetas organizadas por categoría o estado.

- **Exportación**: Permitir exportar notas a PDF o compartirlas por email.

### 5.2 Mejoras Técnicas

- **Record Rules**: Implementar reglas de registro para que los usuarios solo vean sus propias notas privadas.

- **Campos computados adicionales**: Contador de líneas completadas, porcentaje de progreso.

- **Archivado**: Añadir campo `active` para poder archivar notas sin eliminarlas.

- **Ordenación**: Implementar campo `sequence` para ordenar líneas manualmente.

### 5.3 Mejoras de UX

- **Widget de color para tags**: Mostrar los tags con sus colores en la vista tree.

- **Preview de imagen**: Mostrar miniaturas de las imágenes en la vista lista.

- **Atajos de teclado**: Implementar acciones rápidas para crear notas.

---

## 6. Referencias Bibliográficas

### Documentación Oficial

1. Odoo S.A. (2024). *Odoo 17 Developer Documentation*. Recuperado de: https://www.odoo.com/documentation/17.0/developer.html

2. Odoo S.A. (2024). *ORM API*. Recuperado de: https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html

3. Odoo S.A. (2024). *View Records*. Recuperado de: https://www.odoo.com/documentation/17.0/developer/reference/backend/views.html

### Tutoriales y Recursos

4. Odoo S.A. (2024). *Getting Started - Create a new module*. Recuperado de: https://www.odoo.com/documentation/17.0/developer/tutorials/getting_started.html

5. Cybrosys Technologies. (2024). *Many2many Fields and Its Widgets in Odoo*. Recuperado de: https://www.cybrosys.com/blog/many2many-fields-and-its-widgets-odoo

### Herramientas

6. Docker Inc. (2024). *Docker Documentation*. Recuperado de: https://docs.docker.com/

7. PostgreSQL Global Development Group. (2024). *PostgreSQL Documentation*. Recuperado de: https://www.postgresql.org/docs/

---

## Anexo: Estructura del Módulo

```
sgm_bloc_notas/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── controllers.py
├── demo/
│   └── demo.xml
├── models/
│   ├── __init__.py
│   ├── category.py
│   ├── models.py
│   ├── note.py
│   ├── note_line.py
│   └── tag.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── description/
│       └── icon.png
└── views/
    ├── category_views.xml
    ├── menu.xml
    ├── note_line_views.xml
    ├── note_views.xml
    ├── tag_views.xml
    ├── templates.xml
    └── views.xml
```

---

*Documento generado como parte del proyecto de desarrollo de módulos Odoo para la asignatura de Sistemas de Gestión Empresarial.*
