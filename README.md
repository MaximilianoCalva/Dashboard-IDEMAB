# IDEMAB - Instituto Internacional de Medicina Alternativa para el Bienestar

## Información Institucional

**Nombre Completo:** Instituto Internacional de Medicina Alternativa para el Bienestar  
**Acrónimo:** IDEMAB  
**Sitio Web:** https://idemab.com  
**Panel:** https://panel.idemab.com

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDEMAB - Mi Dashboard | Plataforma de Aprendizaje  
**Descripción Corta:** Accede a tu plataforma de aprendizaje en IDEMAB. Consulta tus diplomados, cursos, certificados y avanza en tu formación.

## Colores Institucionales

### Paleta de Colores
- **Color Primario:** `#1C73BA`
- **Color Secundario:** `#2CAC66`
- **Color Accent:** `#5BC0BE`
- **Gradiente Principal:** `linear-gradient(135deg, #1C73BA 0%, #2CAC66 100%)`

### Colores de Sistema
- **Blanco:** `#FFFFFF`
- **Gris Claro:** `#F5F5F5`
- **Éxito (Verde):** `#10b981`
- **Advertencia (Amarillo):** `#f59e0b`
- **Peligro (Rojo):** `#ef4444`

## URLs del Panel

- **Mi Cuenta:** https://panel.idemab.com/mi-cuenta/
- **Iniciar Sesión:** https://panel.idemab.com/iniciar-sesion/
- **Panel Access:** https://panel.idemab.com/panel-access/

---

## 📋 Estructura de Sección Inicio

La sección inicio del Dashboard IDEMAB está organizada en **13 componentes** que siguen un flujo lógico de navegación:

### 1️⃣ Header y Bienvenida
- **01-dashboard-inicio-IDEMAB.html** - Cápsula de título "DASHBOARD" con indicador de inicio
- **02-bienvenida-IDEMAB.html** - Mensaje de bienvenida personalizado

### 2️⃣ Avisos para Administrativos y Docentes
- **03-aviso-admin-docentes-IDEMAB.html** 👥 - Aviso de acceso para administrativos y docentes (con flecha)
- **04-accesos-rapidos-IDEMAB.html** ⚡ - Accesos rápidos a herramientas principales

### 3️⃣ Información Institucional
- **05-aviso-solo-visualizacion-IDEMAB.html** 👁️ - Aviso de visualización con opción de requisición
- **06-reglamento-IDEMAB.html** - Visualizador del reglamento institucional
- **07-plataforma-inactiva-IDEMAB.html** - Aviso de plataforma inactiva

### 4️⃣ Sección Administrativa
- **08-aviso-solo-administrativos-IDEMAB.html** 🔒 - Aviso de acceso restringido a administrativos (con flecha)
- **09-informacion-chatbot-IDEMAB.html** - Información del chatbot institucional
- **10-oferta-activa-IDEMAB.html** - Tabla de diplomados, cursos y eventos activos
- **11-requisiciones-IDEMAB.html** 📋 - Formularios de requisiciones
- **12-correos-activos-IDEMAB.html** 📧 - Lista de cuentas de correo activas

### 5️⃣ Sección Estudiantil
- **13-aviso-dashboard-estudiantil-IDEMAB.html** 📚 - Aviso de visualización estudiantil (con flecha)

---

## 🎨 Componentes de Avisos

### Avisos con Flecha Animada ⬇️
1. **03-aviso-admin-docentes-IDEMAB.html** - Color secundario
2. **08-aviso-solo-administrativos-IDEMAB.html** - Rojo (#dc3545)
3. **13-aviso-dashboard-estudiantil-IDEMAB.html** - Color primario

### Avisos sin Flecha
4. **05-aviso-solo-visualizacion-IDEMAB.html** - Amarillo (#ffc107)

---

## 📊 Componentes Principales

### Tablas y Visualizadores
- **10-oferta-activa-IDEMAB.html** - Tabla dinámica conectada a Google Sheets
- **12-correos-activos-IDEMAB.html** - Tabla con cuentas de correo y estadísticas

### Formularios
- **11-requisiciones-IDEMAB.html** - Tarjetas con enlaces a Google Forms

---

## 🎯 Flujo de Navegación

```
┌─────────────────────────────────────┐
│  01 - Dashboard Inicio              │
│  02 - Bienvenida                    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  SECCIÓN ADMIN/DOCENTES             │
│  03 - Aviso Admin/Docentes 👥⬇️     │
│  04 - Accesos Rápidos ⚡            │
│  05 - Aviso Solo Visualización 👁️  │
│  06 - Reglamento                    │
│  07 - Plataforma Inactiva           │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  SECCIÓN ADMINISTRATIVA             │
│  08 - Aviso Solo Administrativos🔒⬇️│
│  09 - Información Chatbot           │
│  10 - Oferta Activa (Tabla)         │
│  11 - Requisiciones                 │
│  12 - Correos Activos               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  SECCIÓN ESTUDIANTIL                │
│  13 - Aviso Dashboard Estudiantil📚⬇│
└─────────────────────────────────────┘
```

---

## 🛠️ Plataforma y Tecnología

### Stack Tecnológico
- **CMS**: WordPress
- **LMS**: LearnDash / Tutor LMS
- **Constructor**: Elementor Pro
- **Hosting**: https://panel.idemab.com

### Implementación de Componentes HTML

Todos los componentes HTML de este proyecto están diseñados para ser implementados en **Elementor** usando el widget HTML.

#### Cómo Usar en Elementor:

1. **Editar Página/Template**
   - Ir a la página del dashboard que deseas editar
   - Abrir con Elementor

2. **Agregar Widget HTML**
   - Buscar "HTML" en el panel de widgets de Elementor
   - Arrastrar el widget a la sección deseada

3. **Copiar y Pegar Código**
   - Abrir el archivo HTML del componente
   - Copiar TODO el contenido (incluyendo `<style>` y `<script>`)
   - Pegar en el widget HTML de Elementor

4. **Guardar y Publicar**
   - Guardar cambios en Elementor
   - Publicar la página

---

## 📝 Notas Importantes

- ✅ Todos los archivos usan los colores institucionales de IDEMAB
- ✅ Diseño responsive para móviles y tablets
- ✅ Avisos con flechas animadas para mejorar UX
- ✅ Numeración secuencial del 01 al 13
- ✅ Sufijo `-IDEMAB` en todos los archivos para identificación
- ✅ Archivo consolidado disponible: `seccion-iniicio.html`

---

## Última Actualización

**Fecha:** 2 de enero de 2026  
**Versión:** 3.0
