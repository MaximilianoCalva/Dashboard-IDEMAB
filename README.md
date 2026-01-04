# IDEMAB - Instituto Internacional de Medicina Alternativa para el Bienestar

## Información Institucional

**Nombre Completo:** Instituto Internacional de Medicina Alternativa para el Bienestar  
**Acrónimo:** IDEMAB  
**Sitio Web:** https://idemab.com  
**Panel:** https://panel.idemab.com

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDEMAB - Panel de Alumnos | Medicina Alternativa y Bienestar
**Descripción Corta:** Plataforma de estudio del Instituto Internacional de Medicina Alternativa para el Bienestar. Tu espacio para formarte en salud holística y terapias complementarias.

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

## Contacto

**Web Principal:** https://idemab.com

## URLs del Panel

- **Mi Cuenta:** https://panel.idemab.com/mi-cuenta/
- **Iniciar Sesión:** https://panel.idemab.com/iniciar-sesion/
- **Panel Access:** https://panel.idemab.com/panel-access/

## Componentes: Headers & Navegación

### Headers (Optimizados Tablet/Mobile 1024px)
Sistema de headers responsivos con menú hamburguesa para dispositivos con ancho menor a 1024px (tablets y móviles).

#### 1. Header Logged In (Usuario Autenticado)
**Archivo:** `Header/header-logged-in-IDEMAB.html`

- **Marca:** Logo/Texto "IDEMAB" clickeable (redirige a https://idemab.com).
- **Desktop (>1024px):** Botones visibles:
  - 📊 Dashboard
  - 💬 Soporte (WhatsApp)
  - 🚪 Cerrar Sesión
- **Tablet/Móvil (≤1024px):** Menú hamburguesa lateral con overlay.

#### 2. Header Logged Out (Usuario No Autenticado)
**Archivo:** `Header/header-logged-out-IDEMAB.html`

- **Marca:** Logo/Texto clickeable.
- **Acción:** Botón "Acceso a tu diplomado".
- **Responsive:** Menú hamburguesa en tablet/móvil.

#### 3. Header Web Principal
**Archivo:** `header-idemab.html` (en repo web)
- Navegación completa del sitio web.
- Breakpoint 1024px para menú móvil.
- Dropdowns complejos y responsivos.

### Implementación Técnica
- **Breakpoint JS/CSS:** 1024px.
- **Z-Index:** Header (1000), Overlay (998), Menú Lateral (999).

---

## Estructura de Sección Inicio (Dashboard)

La sección inicio del Dashboard IDEMAB está organizada en **13 componentes**:

### 1️⃣ Header y Bienvenida
- **01-dashboard-inicio-IDEMAB.html** - Título "DASHBOARD".
- **02-bienvenida-IDEMAB.html** - Mensaje de bienvenida.

### 2️⃣ Avisos y Accesos
- **03-aviso-admin-docentes-IDEMAB.html** 👥 - Aviso docentes.
- **04-accesos-rapidos-IDEMAB.html** ⚡ - Accesos rápidos.
- **05-aviso-solo-visualizacion-IDEMAB.html** 👁️ - Solo visualización.
- **06-reglamento-IDEMAB.html** - Reglamento.
- **07-plataforma-inactiva-IDEMAB.html** - Aviso inactiva.

### 3️⃣ Sección Administrativa
- **08-aviso-solo-administrativos-IDEMAB.html** 🔒 - Aviso admin.
- **09-informacion-chatbot-IDEMAB.html** - Chatbot.
- **10-oferta-activa-IDEMAB.html** - Tabla oferta activa.
- **11-requisiciones-IDEMAB.html** 📋 - Formularios requisiciones.
- **12-correos-activos-IDEMAB.html** 📧 - Correos activos.

### 4️⃣ Sección Estudiantil
- **13-aviso-dashboard-estudiantil-IDEMAB.html** 📚 - Aviso estudiantil.

---

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`
**Archivo principal:** `extras-grid-idemab.html`

Grid de recursos con 6 secciones idéntico al sistema central pero con colores IDEMAB (#1C73BA).

---

## 🛠️ Cómo Usar en Elementor

1. **Editar Página**: Usar Elementor.
2. **Widget HTML**: Arrastrar widget HTML.
3. **Pegar Código**: Copiar TODO el contenido del archivo HTML (incluyendo `<style>` y `<script>`).
4. **Guardar**: Publicar cambios.

---

**Versión:** 4.0 (Update Headers 1024px)
**Fecha:** Enero 2026
