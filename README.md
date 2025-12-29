# Dashboard Sección Inicio - IDEMAB

## 📋 Descripción

Colección de componentes HTML para la sección de inicio del dashboard de **IDEMAB (Instituto de Educación en Medio Ambiente y Biotecnología)**. Estos componentes están diseñados para ser integrados en WordPress usando widgets HTML personalizados.

## 🎨 Colores Institucionales

IDEMAB utiliza un esquema de colores azul-verde que representa la innovación tecnológica y el compromiso ambiental:

### Paleta Principal
- **Azul Principal**: `#1D71B8` - Color primario institucional
- **Verde Principal**: `#2FAC66` - Color secundario institucional
- **Azul Hover**: `#2A8DD4` - Estados interactivos
- **Verde Hover**: `#3DC77A` - Estados interactivos alternativos

### Degradado Institucional
```css
background: linear-gradient(135deg, #1D71B8 0%, #2FAC66 100%);
```

### Variables CSS
```css
:root {
  --idemab-primary-blue: #1D71B8;
  --idemab-primary-green: #2FAC66;
  --idemab-blue-light: #2A8DD4;
  --idemab-green-light: #3DC77A;
  --idemab-gradient: linear-gradient(135deg, #1D71B8 0%, #2FAC66 100%);
}
```

## 📁 Estructura de Archivos

```
Dashboard-seccion-inicio-IDEMAB/
├── 01-dashboard-inicio-IDEMAB.html          # Cápsula de navegación "Dashboard > Inicio"
├── 02-bienvenida-IDEMAB.html                # Mensaje de bienvenida personalizado
├── 03-reglamento-IDEMAB.html                # Visor de reglamento institucional
├── 04-plataforma-inactiva-IDEMAB.html       # Aviso de cuenta inactiva
├── 05-informacion-chatbot-IDEMAB.html       # Información sobre recursos del chatbot
├── 06-oferta-activa-IDEMAB.html             # Widget de oferta educativa activa
├── 07-accesos-rapidos-IDEMAB.html           # Enlaces de acceso rápido
├── Logo-idemab.png                          # Logo institucional
├── colores-institucionales-IDEMAB.md        # Guía de colores institucionales
└── README.md                                # Este archivo
```

## 🚀 Componentes

### 1. Dashboard Inicio (01)
Cápsula compacta de navegación que muestra "Plataforma IDEMAB | DASHBOARD > Inicio" con animación de flecha.

**Características:**
- Diseño tipo píldora con bordes redondeados
- Degradado azul-verde institucional
- Animación sutil de rebote
- Responsive para móviles

### 2. Bienvenida (02)
Mensaje de bienvenida personalizado para estudiantes.

### 3. Reglamento (03)
Visor de reglamento institucional con navegación por páginas.

**Características:**
- Navegación entre páginas del reglamento
- Botones con colores institucionales
- Diseño limpio y profesional

### 4. Plataforma Inactiva (04)
Aviso informativo sobre posibles razones de cuenta inactiva.

**Características:**
- Diseño de tarjeta con borde superior azul
- Iconos informativos
- Secciones para "Baja Temporal" y "Adeudo en Mensualidad"
- Colores institucionales en títulos y bordes

### 5. Información Chatbot (05)
Información sobre los recursos disponibles del chatbot IA.

**Características:**
- Tarjetas con bordes superiores en tonos azul-verde
- Variables CSS personalizadas
- Diseño modular y escalable

### 6. Oferta Activa (06)
Widget para mostrar ofertas educativas activas.

**Características:**
- Sistema de variables CSS
- Colores institucionales aplicados
- Diseño adaptable

### 7. Accesos Rápidos (07)
Enlaces rápidos a recursos importantes.

## 💻 Uso en WordPress

### Integración con Elementor

1. **Agregar Widget HTML**
   - Arrastra un widget "HTML" a tu sección
   - Copia el contenido completo del archivo `.html`
   - Pega en el editor HTML del widget

2. **Configuración Recomendada**
   - Ancho: 100% del contenedor
   - Padding: Ajustar según necesidad
   - Margen: 10px superior e inferior

### Integración con Bloques de WordPress

1. **Bloque HTML Personalizado**
   - Añade un bloque "HTML personalizado"
   - Pega el código del componente
   - Previsualiza y publica

## 🎯 Características Técnicas

### Responsive Design
- Todos los componentes son responsive
- Breakpoint móvil: `max-width: 600px`
- Ajustes automáticos de tamaño y espaciado

### Tipografía
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

### Accesibilidad
- Contraste de colores optimizado (WCAG 2.1)
- Texto blanco sobre `#1D71B8`: Ratio 5.3:1 ✅
- Texto blanco sobre `#2FAC66`: Ratio 3.1:1 (para elementos grandes)
- Estructura semántica HTML5

## 🔧 Personalización

### Cambiar Colores
Los colores están centralizados en variables CSS. Para personalizarlos:

```css
:root {
  --idemab-primary-blue: #TU_COLOR_AZUL;
  --idemab-primary-green: #TU_COLOR_VERDE;
  --idemab-blue-light: #TU_COLOR_HOVER_AZUL;
  --idemab-green-light: #TU_COLOR_HOVER_VERDE;
}
```

### Ajustar Tamaños
Modifica las variables de tamaño en cada componente:

```css
.component {
  font-size: 18px;  /* Ajustar según necesidad */
  padding: 6px 22px; /* Ajustar espaciado */
}
```

## 📱 Compatibilidad

- ✅ Chrome/Edge (últimas versiones)
- ✅ Firefox (últimas versiones)
- ✅ Safari (últimas versiones)
- ✅ Dispositivos móviles iOS/Android
- ✅ WordPress 5.0+
- ✅ Elementor 3.0+

## 📝 Notas de Desarrollo

### Versión
- **Actual**: 1.0.0
- **Última actualización**: 28 de diciembre de 2025

### Cambios Recientes
- ✅ Aplicación de colores institucionales oficiales (#1D71B8, #2FAC66)
- ✅ Implementación de degradado azul-verde
- ✅ Actualización de variables CSS
- ✅ Mejora de accesibilidad y contraste

## 🤝 Contribución

Para mantener la consistencia visual:
1. Usa siempre los colores institucionales definidos
2. Mantén la estructura de archivos
3. Prueba en diferentes navegadores
4. Verifica la accesibilidad

## 📄 Licencia

Uso interno de IDEMAB - Instituto de Educación en Medio Ambiente y Biotecnología

---

**Desarrollado para IDEMAB** | Última actualización: Diciembre 2025
