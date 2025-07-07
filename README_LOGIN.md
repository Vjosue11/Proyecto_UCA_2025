# 🏪 Sistema de Supermercado - Login Modernizado

## ✨ Características del Nuevo Login

### 🎨 Diseño Moderno
- **Paleta de colores moderna**: Utiliza una paleta de colores profesional con gradientes suaves
- **Tipografía mejorada**: Fuente Segoe UI para mejor legibilidad
- **Iconos emoji**: Uso de emojis para mejorar la experiencia visual
- **Efectos hover**: Los botones cambian de color al pasar el mouse

### 🔧 Funcionalidades Mejoradas

#### Login Principal
- **Ventana centrada**: Se posiciona automáticamente en el centro de la pantalla
- **Placeholders inteligentes**: Texto de ayuda que desaparece al escribir
- **Validaciones mejoradas**: Mensajes de error más claros y específicos
- **Atajos de teclado**: 
  - `Enter` para iniciar sesión
  - `Escape` para salir

#### Registro de Usuarios
- **Formulario expandido**: Más espacio para los campos
- **Validación de contraseña**: Mínimo 4 caracteres
- **Campo de clave especial**: Aparece solo cuando se selecciona "admin"
- **Mensajes de éxito/error**: Con iconos para mejor feedback

### 🎯 Mejoras de UX

#### Campos de Entrada
- **Bordes modernos**: Diseño limpio con bordes sutiles
- **Focus automático**: El cursor se posiciona automáticamente
- **Selección de texto**: Al hacer focus, se selecciona todo el contenido
- **Placeholders dinámicos**: Texto de ayuda que se comporta como placeholder

#### Botones
- **Estilo flat**: Diseño moderno sin relieves
- **Efectos hover**: Cambio de color al pasar el mouse
- **Cursor pointer**: Indica que son elementos clickeables
- **Colores semánticos**: Verde para éxito, rojo para cancelar

### 🎨 Paleta de Colores

```python
LOGIN_COLORS = {
    'primary': '#667eea',      # Azul principal
    'secondary': '#764ba2',    # Púrpura secundario
    'background': '#f8fafc',   # Fondo gris claro
    'surface': '#ffffff',      # Superficie blanca
    'text': '#2d3748',         # Texto principal
    'text_secondary': '#718096', # Texto secundario
    'border': '#e2e8f0',       # Bordes
    'success': '#48bb78',      # Verde éxito
    'error': '#f56565',        # Rojo error
    'warning': '#ed8936'       # Naranja advertencia
}
```

### 🚀 Cómo Usar

1. **Ejecutar la aplicación**:
   ```bash
   cd prueba
   python main.py
   ```

2. **Usuarios de prueba**:
   - **Administrador**: `admin` / `admin`
   - **Usuario**: `usuario` / `usuario`

3. **Registrar nuevo usuario**:
   - Hacer clic en "📝 CREAR CUENTA"
   - Completar el formulario
   - Para admin, usar clave especial: `claveadmin2025`

### 🔧 Funciones Principales

#### `crear_boton_moderno()`
Crea botones con estilo moderno y efectos hover.

#### `crear_entry_moderno()`
Crea campos de entrada con placeholders y validación.

#### `mostrar_login()`
Ventana principal de login con diseño moderno.

#### `mostrar_registro_ventana()`
Ventana de registro con validaciones mejoradas.

### 📱 Responsive Design
- **Ventanas redimensionadas**: Tamaños optimizados para mejor visualización
- **Espaciado consistente**: Padding y márgenes uniformes
- **Layout flexible**: Se adapta a diferentes tamaños de pantalla

### 🎯 Próximas Mejoras
- [ ] Animaciones suaves
- [ ] Tema oscuro/claro
- [ ] Recuperación de contraseña
- [ ] Validación de email
- [ ] Captcha para seguridad

---

**Desarrollado con ❤️ usando Python y Tkinter** 