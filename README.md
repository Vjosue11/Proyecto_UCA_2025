# 🏪 Sistema de Gestión de Supermercado

## Descripción General

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando Tkinter para la gestión de inventario y usuarios en un supermercado. Permite el registro, autenticación y administración de productos, así como el control de movimientos de entrada y salida de inventario. Incluye un sistema de login moderno y seguro, con roles de usuario y administrador.

---

## 📁 Estructura de Archivos

- `main.py`: Interfaz gráfica principal. Incluye el login, registro de usuarios, panel de administración y usuario, y todas las operaciones sobre productos y movimientos.
- `productos_datos.py`: Módulo de acceso a datos. Gestiona operaciones CRUD sobre productos, búsqueda, sugerencias y autenticación de usuarios.
- `conexion.py`: Maneja la conexión a la base de datos SQLite y la creación automática de las tablas necesarias.
- `test_login.py`: Script de prueba para verificar el funcionamiento del login y la importación de módulos.
- `supermercado.db`: Base de datos SQLite con las tablas de productos, movimientos y usuarios.
- `README_LOGIN.md`: Documentación específica sobre el sistema de login modernizado.
- `auth.py`: (Vacío, reservado para futuras funcionalidades de autenticación avanzada).

---

## 🚀 ¿Cómo ejecutar la aplicación?

1. **Instala las dependencias necesarias** (si no tienes Tkinter, viene por defecto con la mayoría de instalaciones de Python):
   ```bash
   pip install tk
   ```

2. **Ejecuta la aplicación**:
   ```bash
   cd prueba
   python main.py
   ```

3. **Usuarios de prueba**:
   - Administrador: `admin` / `admin`
   - Usuario: `usuario` / `usuario`

4. **Registrar nuevo usuario**:
   - Haz clic en "📝 CREAR CUENTA"
   - Completa el formulario
   - Para admin, usa la clave especial: `claveadmin2025`

---

## 🛠️ Funcionalidades principales

- **Login y registro moderno**: Interfaz atractiva, validaciones, roles de usuario y administrador.
- **Gestión de productos**: Alta, baja, modificación y consulta de productos con control de stock bajo.
- **Movimientos de inventario**: Registro de entradas y salidas de productos.
- **Búsqueda y sugerencias**: Autocompletado y sugerencias inteligentes al buscar productos.
- **Base de datos persistente**: Todo se almacena en `supermercado.db`.

---

## 📦 Módulos principales

### `main.py`
- Ventana principal de login y registro.
- Panel de administración y usuario.
- Gestión visual de productos y movimientos.
- Uso de colores modernos y UX mejorada.

### `productos_datos.py`
- Funciones para guardar, consultar, actualizar y eliminar productos.
- Búsqueda de productos con sugerencias.
- Autenticación de usuarios.
- Consulta de productos con stock bajo.

### `conexion.py`
- Conexión a la base de datos SQLite.
- Creación automática de tablas si no existen.
- Inserción de usuarios por defecto si la base está vacía.

### `test_login.py`
- Prueba automatizada del sistema de login.
- Verifica la importación y funcionamiento de la ventana de login.

### `auth.py`
- Archivo vacío, reservado para futuras mejoras de autenticación.

---

## 💡 Próximas mejoras sugeridas
- Animaciones suaves en la interfaz.
- Tema oscuro/claro.
- Recuperación de contraseña.
- Validación de email.
- Captcha para mayor seguridad.

---

**Desarrollado con ❤️ en Python y Tkinter.** 