# Colores Institucionales - IDEMAB

Este documento define la paleta de colores oficial del Instituto de Educación en Medio Ambiente y Biotecnología.

---

## 🧪 IDEMAB (Instituto de Educación en Medio Ambiente y Biotecnología)

### Color Principal (Degradado)
- **Azul**: `#1D71B8`
  - **RGB**: `rgb(29, 113, 184)`
  - **HSL**: `hsl(208, 73%, 42%)`

- **Verde**: `#2FAC66`
  - **RGB**: `rgb(47, 172, 102)`
  - **HSL**: `hsl(146, 57%, 43%)`

### Degradado Institucional
```css
background: linear-gradient(135deg, #1D71B8 0%, #2FAC66 100%);
```

### Colores Complementarios
- **Blanco**: `#FFFFFF`
- **Gris Claro**: `#F5F5F5`
- **Gris Medio**: `#E0E0E0`
- **Texto Oscuro**: `#2C3E50`
- **Azul Claro** (para hover): `#2A8DD4`
- **Verde Claro** (para hover): `#3DC77A`

---

## 🎨 Uso Recomendado

- **Encabezados y CTAs**: Degradado (#1D71B8 → #2FAC66)
- **Fondos de secciones**: Azul (#1D71B8) o Verde (#2FAC66)
- **Texto sobre fondos oscuros**: Blanco (#FFFFFF)
- **Texto general**: Texto Oscuro (#2C3E50)
- **Estados hover**: Azul Claro (#2A8DD4) o Verde Claro (#3DC77A)

---

## 📋 Implementación CSS

```css
:root {
  /* IDEMAB Colors */
  --idemab-primary-blue: #1D71B8;
  --idemab-primary-green: #2FAC66;
  --idemab-blue-light: #2A8DD4;
  --idemab-green-light: #3DC77A;
  --idemab-white: #FFFFFF;
  --idemab-light-gray: #F5F5F5;
  --idemab-medium-gray: #E0E0E0;
  --idemab-dark-text: #2C3E50;
  
  /* Degradado institucional */
  --idemab-gradient: linear-gradient(135deg, #1D71B8 0%, #2FAC66 100%);
}

/* Ejemplo de uso */
.btn-primary {
  background: var(--idemab-gradient);
  color: var(--idemab-white);
  border: none;
}

.btn-primary:hover {
  background: var(--idemab-blue-light);
}

.section-header {
  background: var(--idemab-gradient);
  color: var(--idemab-white);
}

/* Variantes con colores sólidos */
.bg-primary-blue {
  background-color: var(--idemab-primary-blue);
}

.bg-primary-green {
  background-color: var(--idemab-primary-green);
}
```

---

## 📝 Notas de Accesibilidad

### Contraste de Texto
- **Texto blanco sobre #1D71B8**: Ratio de contraste de 5.3:1 ✅ (muy bueno para texto)
- **Texto blanco sobre #2FAC66**: Ratio de contraste de 3.1:1 (bueno para texto grande)
- **Texto blanco sobre #2A8DD4**: Ratio de contraste de 3.8:1 (bueno para texto grande)

### Recomendaciones
- El azul (#1D71B8) tiene excelente contraste con texto blanco
- Para el verde (#2FAC66), usar preferentemente en elementos grandes
- Para fondos claros, usar el color de texto oscuro (#2C3E50)

---

## 🎨 Paleta de Colores

| Color | Hex | Descripción | Uso |
|-------|-----|-------------|-----|
| Azul | `#1D71B8` | Color principal (inicio degradado) | Fondos, degradados |
| Verde | `#2FAC66` | Color principal (fin degradado) | Fondos, degradados |
| Azul Claro | `#2A8DD4` | Hover/Activo | Estados interactivos |
| Verde Claro | `#3DC77A` | Hover/Activo | Estados interactivos |
| Blanco | `#FFFFFF` | Neutro | Fondos, texto sobre oscuro |
| Gris Claro | `#F5F5F5` | Neutro | Fondos alternativos |
| Texto Oscuro | `#2C3E50` | Neutro | Texto principal |

---

**Última actualización**: 28 de diciembre de 2025
