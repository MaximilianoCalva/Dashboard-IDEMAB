# IDEMAB - Instituto Internacional de Medicina Alternativa para el Bienestar

## Información Institucional

**Nombre Completo:** Instituto Internacional de Medicina Alternativa para el Bienestar  
**Acrónimo:** IDEMAB  
**Sitio Web:** https://idemab.com  
**Panel:** https://panel.idemab.com

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDEMAB - Mi Dashboard | Plataforma de Medicina Alternativa  
**Descripción Corta:** Accede a tu plataforma de aprendizaje en Medicina Alternativa. Consulta tus diplomados, cursos, certificados y avanza en tu formación en terapias holísticas.

## Colores Institucionales

### Paleta de Colores
- **Azul Primario:** `#1C73BA`
- **Verde Secundario:** `#2CAC64`

### Colores de Sistema
- **Blanco:** `#FFFFFF`
- **Gris Claro:** `#F5F5F5`
- **Éxito (Verde):** `#10b981`
- **Peligro (Rojo):** `#ef4444`

### Bordes y Sombras
- **Border Color:** `#e3f2fd`
- **Box Shadow:** `0 2px 8px rgba(28, 115, 186, 0.06)`

## Contacto

**WhatsApp Soporte:** +52 33 2924 3805  
**URL WhatsApp:** https://wa.me/5213329243805  
**Canal WhatsApp:** https://whatsapp.com/channel/0029Vb6HP1w5kg7DYe2Djt1d

## Redes Sociales

**Imagen de Cuentas Oficiales:** https://idemab.com/wp-content/uploads/2025/01/Cuentas-reales-Post-05.jpg

## URLs del Panel

- **Mi Cuenta:** https://panel.idemab.com/mi-cuenta/
- **Iniciar Sesión:** https://panel.idemab.com/iniciar-sesion/
- **Logout:** https://panel.idemab.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fpanel.idemab.com

## Componentes del Dashboard

### Headers
- `Header/header-logged-in-IDEMAB.html` - Header para usuarios autenticados
- `Header/header-logged-out-IDEMAB.html` - Header para usuarios no autenticados

### Especificaciones del Header
- **Padding:** 3px 10px
- **Ancho:** 100% (full width)
- **Altura Mínima:** 50px
- **Font Size Brand:** 18px (desktop), 16px (mobile)
- **Font Size Subtitle:** 9px (desktop), 7-8px (mobile)
- **Color Brand:** Azul primario (#1C73BA)

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

#### Componentes Disponibles:

**Headers**:
- `Header/header-logged-in-IDEMAB.html` - Header para usuarios autenticados
- `Header/header-logged-out-IDEMAB.html` - Header para usuarios no autenticados

**Extras**:
- `Extras/extras-grid-idemab.html` - Grid de recursos adicionales (Biblioteca Reiki, Videoteca Reiki, Videoteca UCDM)

**Acceso**:
- `Acceso a dashboard/login-idemab-snippet.html` - Página de login
- `Acceso a dashboard/logout-idemab-snippet.html` - Página de logout

---

## Última Actualización

Fecha: 2026-01-01  
Versión: 2.0

## Archivos de Acceso al Dashboard

### Carpeta: `Acceso a dashboard/`

**Para usuarios autenticados (logged-in):**
- `login-idemab-snippet.html` - Página de bienvenida con botón "Ir al Dashboard"
  - Redirige a: `https://panel.idemab.com/plataforma/`

**Para usuarios NO autenticados (logged-out):**
- `logout-idemab-snippet.html` - Formulario de inicio de sesión
  - Contiene shortcode: `[profilepress-login id="1"]`
  - Incluye instrucciones para el usuario

**Uso en WordPress:**
- Copiar y pegar el contenido completo en un widget HTML de Elementor
- Los snippets no afectan el diseño de la página existente
- Usan clases CSS únicas para evitar conflictos

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`

**Archivo principal:** `extras-grid-idemab.html`

Grid de recursos adicionales con 3 secciones organizadas por programa:

1. **📚 Biblioteca Reiki**
   - URL: https://panel.idemab.com/biblioteca-dr/
   - Biblioteca del Diplomado en Reiki
   - Badge: "Diplomado Reiki"

2. **🎥 Videoteca Reiki**
   - URL: https://panel.idemab.com/videoteca-dr/
   - Videos del Diplomado en Reiki
   - Badge: "Diplomado Reiki"

3. **🎬 Videoteca UCDM**
   - URL: https://panel.idemab.com/videoteca-ucdm/
   - Videos de Un Curso de Milagros
   - Badge: "Un Curso de Milagros"

### Diseño de Extras
- **Colores**: Gradiente azul IDEMAB (#1C73BA a #2196F3)
- **Layout**: Grid responsive (3 columnas desktop, 1 mobile)
- **Badges**: Identificadores de programa en cada tarjeta
- **Interactividad**: Hover effects con elevación y sombra
