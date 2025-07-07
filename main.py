import tkinter as tk
from tkinter import ttk, messagebox, END, BOTH, X, Y, W, CENTER, NO, LEFT, RIGHT, YES, Listbox, Menu
import re
from productos_datos import save, findAll, update, delete, find_low_stock, search_suggestions, autenticar_usuario
from datetime import datetime
import conexion

CLAVE_ADMIN = "claveadmin2025"  # Cambia esto por la clave especial que desees

# =====================
# LOGIN Y REGISTRO MODERNIZADO
# =====================

# Colores modernos para el login
LOGIN_COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'background': '#f8fafc',
    'surface': '#ffffff',
    'text': '#2d3748',
    'text_secondary': '#718096',
    'border': '#e2e8f0',
    'success': '#48bb78',
    'error': '#f56565',
    'warning': '#ed8936'
}

def crear_boton_moderno(parent, text, command, bg_color=LOGIN_COLORS['primary'], fg_color='white', width=20, height=2):
    """Crea un botón con estilo moderno"""
    btn = tk.Button(parent, text=text, command=command, 
                   bg=bg_color, fg=fg_color, 
                   font=('Segoe UI', 11, 'bold'),
                   relief='flat', borderwidth=0,
                   width=width, height=height,
                   cursor='hand2')
    
    def on_enter(e):
        btn['bg'] = '#5a67d8' if bg_color == LOGIN_COLORS['primary'] else '#e53e3e'
    
    def on_leave(e):
        btn['bg'] = bg_color
    
    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)
    return btn

def crear_entry_moderno(parent, show="", placeholder=""):
    """Crea un campo de entrada con estilo moderno"""
    frame = tk.Frame(parent, bg=LOGIN_COLORS['surface'], relief='solid', borderwidth=1)
    
    entry = tk.Entry(frame, show=show, font=('Segoe UI', 11),
                    bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                    relief='flat', borderwidth=0,
                    insertbackground=LOGIN_COLORS['primary'])
    
    entry.pack(fill='both', expand=True, padx=10, pady=8)
    
    # Placeholder effect
    if placeholder:
        entry.insert(0, placeholder)
        entry.config(fg=LOGIN_COLORS['text_secondary'])
        
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg=LOGIN_COLORS['text'])
        
        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg=LOGIN_COLORS['text_secondary'])
        
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)
    
    return frame, entry

def mostrar_login():
    login_win = tk.Tk()
    login_win.title("Sistema de Supermercado - Login")
    login_win.geometry("450x650")
    login_win.resizable(False, False)
    login_win.configure(bg=LOGIN_COLORS['background'])
    
    # Centrar la ventana
    login_win.update_idletasks()
    x = (login_win.winfo_screenwidth() // 2) - (450 // 2)
    y = (login_win.winfo_screenheight() // 2) - (650 // 2)
    login_win.geometry(f"450x650+{x}+{y}")
    
    # Frame principal con sombra
    main_frame = tk.Frame(login_win, bg=LOGIN_COLORS['surface'], 
                         relief='solid', borderwidth=1)
    main_frame.pack(fill='both', expand=True, padx=15, pady=15)
    
    # Header con título
    header_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    header_frame.pack(fill='x', pady=(25, 15))
    
    # Título principal
    title_label = tk.Label(header_frame, text="🏪 SISTEMA DE SUPERMERCADO", 
                          font=('Segoe UI', 16, 'bold'),
                          bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['primary'])
    title_label.pack()
    
    subtitle_label = tk.Label(header_frame, text="Iniciar Sesión", 
                             font=('Segoe UI', 11),
                             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text_secondary'])
    subtitle_label.pack(pady=(3, 0))
    
    # Formulario
    form_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    form_frame.pack(fill='x', padx=30, pady=15)
    
    # Usuario
    tk.Label(form_frame, text="👤 Usuario", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 3))
    
    user_frame, entry_user = crear_entry_moderno(form_frame, show="", placeholder="Ingrese su usuario")
    user_frame.pack(fill='x', pady=(0, 12))
    
    # Contraseña
    tk.Label(form_frame, text="🔒 Contraseña", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 3))
    
    pass_frame, entry_pass = crear_entry_moderno(form_frame, show="*", placeholder="Ingrese su contraseña")
    pass_frame.pack(fill='x', pady=(0, 12))
    
    # Tipo de usuario con checkboxes
    tk.Label(form_frame, text="👥 Tipo de Usuario", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 5))
    
    tipo_var = tk.StringVar(value="usuario")
    tipo_frame = tk.Frame(form_frame, bg=LOGIN_COLORS['surface'])
    tipo_frame.pack(fill='x', pady=(0, 15))
    
    # Checkbox para Usuario
    def on_usuario_click():
        if usuario_var.get():
            admin_var.set(False)
            tipo_var.set("usuario")
        else:
            usuario_var.set(True)  # Mantener al menos uno seleccionado
    
    def on_admin_click():
        if admin_var.get():
            usuario_var.set(False)
            tipo_var.set("admin")
        else:
            admin_var.set(True)  # Mantener al menos uno seleccionado
    
    usuario_var = tk.BooleanVar(value=True)
    admin_var = tk.BooleanVar(value=False)
    
    # Frame para checkboxes
    checkbox_frame = tk.Frame(tipo_frame, bg=LOGIN_COLORS['surface'])
    checkbox_frame.pack(fill='x')
    
    # Checkbox Usuario
    usuario_check = tk.Checkbutton(checkbox_frame, text="👤 Usuario", 
                                  variable=usuario_var, 
                                  command=on_usuario_click,
                                  font=('Segoe UI', 10),
                                  bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                                  selectcolor=LOGIN_COLORS['primary'],
                                  activebackground=LOGIN_COLORS['surface'],
                                  activeforeground=LOGIN_COLORS['text'])
    usuario_check.pack(side='left', padx=(0, 20))
    
    # Checkbox Admin
    admin_check = tk.Checkbutton(checkbox_frame, text="👑 Administrador", 
                                variable=admin_var, 
                                command=on_admin_click,
                                font=('Segoe UI', 10),
                                bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                                selectcolor=LOGIN_COLORS['primary'],
                                activebackground=LOGIN_COLORS['surface'],
                                activeforeground=LOGIN_COLORS['text'])
    admin_check.pack(side='left')
    
    # Botones
    buttons_frame = tk.Frame(form_frame, bg=LOGIN_COLORS['surface'])
    buttons_frame.pack(fill='x', pady=10)
    
    def intentar_login():
        user = entry_user.get().strip()
        pwd = entry_pass.get().strip()
        tipo = tipo_var.get()
        
        # Validaciones
        if not user or user == "Ingrese su usuario":
            messagebox.showerror("Error", "Por favor ingrese un usuario")
            return
        if not pwd or pwd == "Ingrese su contraseña":
            messagebox.showerror("Error", "Por favor ingrese una contraseña")
            return
        
        tipo_autenticado = autenticar_usuario(user, pwd)
        if tipo_autenticado == tipo:
            login_win.destroy()
            iniciar_aplicacion(tipo, user)
        elif tipo_autenticado is not None:
            messagebox.showerror("Acceso denegado", 
                               f"El usuario existe pero no es del tipo seleccionado: {tipo}")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def mostrar_registro():
        login_win.withdraw()
        mostrar_registro_ventana(login_win)

    # Botón de login
    login_btn = crear_boton_moderno(buttons_frame, "🚀 INICIAR SESIÓN", intentar_login)
    login_btn.pack(fill='x', pady=(0, 8))
    
    # Separador
    separator = tk.Frame(buttons_frame, height=1, bg=LOGIN_COLORS['border'])
    separator.pack(fill='x', pady=8)
    
    # Botón de registro
    register_btn = crear_boton_moderno(buttons_frame, "📝 CREAR CUENTA", mostrar_registro, 
                                     LOGIN_COLORS['secondary'])
    register_btn.pack(fill='x')
    
    # Footer
    footer_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    footer_frame.pack(fill='x', pady=(15, 20))
    
    footer_label = tk.Label(footer_frame, text="© 2025 Sistema de Supermercado", 
                           font=('Segoe UI', 8),
                           bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text_secondary'])
    footer_label.pack()
    
    # Configurar eventos
    entry_user.focus_set()
    login_win.bind('<Return>', lambda e: intentar_login())
    login_win.bind('<Escape>', lambda e: login_win.destroy())
    
    login_win.mainloop()


def mostrar_registro_ventana(parent_win):
    reg_win = tk.Toplevel()
    reg_win.title("Sistema de Supermercado - Registro")
    reg_win.geometry("500x700")
    reg_win.resizable(False, False)
    reg_win.configure(bg=LOGIN_COLORS['background'])
    
    # Centrar la ventana
    reg_win.update_idletasks()
    x = (reg_win.winfo_screenwidth() // 2) - (500 // 2)
    y = (reg_win.winfo_screenheight() // 2) - (700 // 2)
    reg_win.geometry(f"500x700+{x}+{y}")
    
    # Frame principal
    main_frame = tk.Frame(reg_win, bg=LOGIN_COLORS['surface'], 
                         relief='solid', borderwidth=1)
    main_frame.pack(fill='both', expand=True, padx=15, pady=15)
    
    # Header
    header_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    header_frame.pack(fill='x', pady=(25, 15))
    
    title_label = tk.Label(header_frame, text="📝 NUEVO USUARIO", 
                          font=('Segoe UI', 16, 'bold'),
                          bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['primary'])
    title_label.pack()
    
    subtitle_label = tk.Label(header_frame, text="Complete los datos para registrarse", 
                             font=('Segoe UI', 11),
                             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text_secondary'])
    subtitle_label.pack(pady=(3, 0))
    
    # Formulario
    form_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    form_frame.pack(fill='x', padx=30, pady=15)
    
    # Usuario
    tk.Label(form_frame, text="👤 Nuevo Usuario", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 3))
    
    user_frame, entry_user = crear_entry_moderno(form_frame, show="", placeholder="Ingrese el nombre de usuario")
    user_frame.pack(fill='x', pady=(0, 12))
    
    # Contraseña
    tk.Label(form_frame, text="🔒 Contraseña", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 3))
    
    pass_frame, entry_pass = crear_entry_moderno(form_frame, show="*", placeholder="Ingrese la contraseña")
    pass_frame.pack(fill='x', pady=(0, 12))
    
    # Tipo de usuario con checkboxes
    tk.Label(form_frame, text="👥 Tipo de Usuario", 
             font=('Segoe UI', 10, 'bold'),
             bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
             anchor='w').pack(fill='x', pady=(0, 5))
    
    tipo_var = tk.StringVar(value="usuario")
    tipo_frame = tk.Frame(form_frame, bg=LOGIN_COLORS['surface'])
    tipo_frame.pack(fill='x', pady=(0, 12))
    
    # Checkbox para Usuario
    def on_usuario_click():
        if usuario_var.get():
            admin_var.set(False)
            tipo_var.set("usuario")
            clave_admin_label.pack_forget()
            clave_admin_frame.pack_forget()
        else:
            usuario_var.set(True)  # Mantener al menos uno seleccionado
    
    def on_admin_click():
        if admin_var.get():
            usuario_var.set(False)
            tipo_var.set("admin")
            clave_admin_label.pack(fill='x', pady=(0, 3))
            clave_admin_frame.pack(fill='x', pady=(0, 12))
        else:
            admin_var.set(True)  # Mantener al menos uno seleccionado
    
    usuario_var = tk.BooleanVar(value=True)
    admin_var = tk.BooleanVar(value=False)
    
    # Frame para checkboxes
    checkbox_frame = tk.Frame(tipo_frame, bg=LOGIN_COLORS['surface'])
    checkbox_frame.pack(fill='x')
    
    # Checkbox Usuario
    usuario_check = tk.Checkbutton(checkbox_frame, text="👤 Usuario", 
                                  variable=usuario_var, 
                                  command=on_usuario_click,
                                  font=('Segoe UI', 10),
                                  bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                                  selectcolor=LOGIN_COLORS['primary'],
                                  activebackground=LOGIN_COLORS['surface'],
                                  activeforeground=LOGIN_COLORS['text'])
    usuario_check.pack(side='left', padx=(0, 20))
    
    # Checkbox Admin
    admin_check = tk.Checkbutton(checkbox_frame, text="👑 Administrador", 
                                variable=admin_var, 
                                command=on_admin_click,
                                font=('Segoe UI', 10),
                                bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                                selectcolor=LOGIN_COLORS['primary'],
                                activebackground=LOGIN_COLORS['surface'],
                                activeforeground=LOGIN_COLORS['text'])
    admin_check.pack(side='left')
    
    # Clave especial para admin (inicialmente oculta)
    clave_admin_label = tk.Label(form_frame, text="🔑 Clave Especial de Administrador", 
                                font=('Segoe UI', 10, 'bold'),
                                bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text'],
                                anchor='w')
    clave_admin_frame, clave_admin_entry = crear_entry_moderno(form_frame, show="*", 
                                                              placeholder="Ingrese la clave especial")

    def registrar():
        user = entry_user.get().strip()
        pwd = entry_pass.get().strip()
        tipo = tipo_var.get()
        
        # Validaciones
        if not user or user == "Ingrese el nombre de usuario":
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario")
            return
        if not pwd or pwd == "Ingrese la contraseña":
            messagebox.showerror("Error", "Por favor ingrese una contraseña")
            return
        if len(pwd) < 4:
            messagebox.showerror("Error", "La contraseña debe tener al menos 4 caracteres")
            return
        
        if tipo == "admin":
            clave = clave_admin_entry.get().strip()
            if not clave or clave == "Ingrese la clave especial":
                messagebox.showerror("Error", "Por favor ingrese la clave especial de administrador")
                return
            if clave != CLAVE_ADMIN:
                messagebox.showerror("Error", "Clave especial de administrador incorrecta")
                return
        
        # Insertar usuario en la base de datos
        try:
            db = conexion.conectar()
            if db is None:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos")
                return
            cursor = db.cursor()
            # Usar columna es_admin para compatibilidad
            es_admin = 1 if tipo == "admin" else 0
            cursor.execute("INSERT INTO usuarios (username, password, es_admin) VALUES (?, ?, ?)", (user, pwd, es_admin))
            db.commit()
            messagebox.showinfo("✅ Éxito", "Usuario registrado correctamente")
            reg_win.destroy()
            parent_win.deiconify()
        except Exception as ex:
            if "UNIQUE" in str(ex):
                messagebox.showerror("❌ Error", "El nombre de usuario ya existe")
            else:
                messagebox.showerror("❌ Error", f"No se pudo registrar: {str(ex)}")
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'db' in locals() and db is not None: db.close()

    # Botones
    buttons_frame = tk.Frame(form_frame, bg=LOGIN_COLORS['surface'])
    buttons_frame.pack(fill='x', pady=20)
    
    # Botón de registro
    register_btn = crear_boton_moderno(buttons_frame, "✅ REGISTRAR USUARIO", registrar)
    register_btn.pack(fill='x', pady=(0, 10))
    
    # Separador
    separator = tk.Frame(buttons_frame, height=1, bg=LOGIN_COLORS['border'])
    separator.pack(fill='x', pady=10)
    
    # Botón de cancelar
    cancel_btn = crear_boton_moderno(buttons_frame, "❌ CANCELAR", 
                                   lambda: (reg_win.destroy(), parent_win.deiconify()),
                                   LOGIN_COLORS['error'])
    cancel_btn.pack(fill='x')
    
    # Footer
    footer_frame = tk.Frame(main_frame, bg=LOGIN_COLORS['surface'])
    footer_frame.pack(fill='x', pady=(20, 30))
    
    footer_label = tk.Label(footer_frame, text="© 2025 Sistema de Supermercado", 
                           font=('Segoe UI', 9),
                           bg=LOGIN_COLORS['surface'], fg=LOGIN_COLORS['text_secondary'])
    footer_label.pack()
    
    # Configurar eventos
    entry_user.focus_set()
    reg_win.bind('<Return>', lambda e: registrar())
    reg_win.bind('<Escape>', lambda e: (reg_win.destroy(), parent_win.deiconify()))
    
    reg_win.mainloop()

# =====================
# INTERFAZ ADMIN Y USUARIO
# =====================
def iniciar_aplicacion_admin():
    iniciar_aplicacion("admin", "admin")

def iniciar_aplicacion_usuario():
    iniciar_aplicacion("usuario", "usuario")

def iniciar_aplicacion(tipo_usuario, usuario):
    # Configuración de la ventana principal
    v = tk.Tk()
    v.title(f"Sistema de Supermercado - {'Administrador' if tipo_usuario == 'admin' else 'Usuario'}")
    v.geometry("1200x900")
    v.resizable(True, True)

    # Configuración de estilo moderno
    style = ttk.Style()
    style.theme_use('clam')

    # Colores modernos (tema oscuro claro)
    COLOR_FONDO = "#2d3436"
    COLOR_FONDO_SECUNDARIO = "#636e72"
    COLOR_TEXTO = "#dfe6e9"
    COLOR_BOTONES = "#0984e3"
    COLOR_BOTONES_ACTIVO = "#74b9ff"
    COLOR_ENTRADA = "#b2bec3"
    COLOR_TABLA_HEADER = "#34495e"
    COLOR_TABLA_FILA = "#2c3e50"
    COLOR_TABLA_FILA_ALT = "#34495e"
    COLOR_ALERTA = "#e17055"

    # Configurar estilos
    style.configure('TFrame', background=COLOR_FONDO)
    style.configure('TLabel', background=COLOR_FONDO, foreground=COLOR_TEXTO, font=('Segoe UI', 11))
    style.configure('TButton', background=COLOR_BOTONES, foreground=COLOR_TEXTO, font=('Segoe UI', 10), 
                    borderwidth=1, focusthickness=3, focuscolor='none')
    style.map('TButton', background=[('active', COLOR_BOTONES_ACTIVO)])
    style.configure('TEntry', fieldbackground=COLOR_ENTRADA, font=('Segoe UI', 11), borderwidth=2, relief='solid')
    style.configure('TCombobox', fieldbackground=COLOR_ENTRADA, font=('Segoe UI', 11))
    style.configure('Treeview', background=COLOR_TABLA_FILA, foreground=COLOR_TEXTO, 
                    fieldbackground=COLOR_TABLA_FILA, font=('Segoe UI', 10))
    style.configure('Treeview.Heading', background=COLOR_TABLA_HEADER, foreground=COLOR_TEXTO, 
                    font=('Segoe UI', 10, 'bold'))
    style.map('Treeview', background=[('selected', COLOR_BOTONES)])
    style.configure('TLabelframe', background=COLOR_FONDO, foreground=COLOR_TEXTO)
    style.configure('TLabelframe.Label', background=COLOR_FONDO, foreground=COLOR_TEXTO)

    v.config(bg=COLOR_FONDO)

    # Variables globales
    txt_id = tk.StringVar()
    txt_producto = tk.StringVar()
    txt_precio = tk.StringVar()
    txt_cantidad = tk.StringVar()
    txt_categoria = tk.StringVar()
    txt_descripcion = tk.StringVar()
    txt_tipo_movimiento = tk.StringVar(value="entrada")
    txt_cantidad_movimiento = tk.StringVar(value="1")
    nombre_original = ""
    orden_actual = {"columna": "producto", "ascendente": True}
    sugerencias_listbox = None
    fuente = ("Segoe UI", 11)

    # ==============================================
    # FUNCIONES CRUD
    # ==============================================
    def salir():
        if messagebox.askyesno("Salir", "¿Está seguro de que desea salir?"):
            v.destroy()

    def limpiar():
        global nombre_original
        txt_id.set("")
        txt_producto.set("")
        txt_precio.set("")
        txt_cantidad.set("")
        txt_categoria.set("")
        txt_descripcion.set("")
        txt_cantidad_movimiento.set("1")
        nombre_original = ""
        e_producto.focus()

    def guardar():
        errores = []
        producto = txt_producto.get().strip()
        precio = txt_precio.get().strip()
        cantidad = txt_cantidad.get().strip()
        categoria = txt_categoria.get().strip()

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", producto):
            errores.append("El producto debe contener solo letras y espacios")
        if not precio.isnumeric():
            errores.append("El precio debe ser numérico")
        if not cantidad.isnumeric():
            errores.append("La cantidad debe ser numérica")
        if not categoria:
            errores.append("La categoría no puede estar vacía")

        if errores:
            messagebox.showerror("Error de validación", "\n".join(errores))
            return

        datos = {
            "producto": producto,
            "precio": int(precio),
            "cantidad": int(cantidad),
            "categoria": categoria
        }

        resultado = save(datos)
        if resultado["respuesta"]:
            messagebox.showinfo("Éxito", resultado["mensaje"])
            llenar_tabla_productos()
            limpiar()
        else:
            messagebox.showerror("Error", resultado["mensaje"])

    def buscar():
        global nombre_original
        producto = txt_producto.get().strip()
        if producto:
            res = findAll()
            productos = res.get("producto", [])
            for fila in productos:
                if fila[1].lower() == producto.lower():
                    txt_id.set(fila[0])
                    txt_producto.set(fila[1])
                    txt_precio.set(fila[2])
                    txt_cantidad.set(fila[3])
                    txt_categoria.set(fila[4])
                    nombre_original = fila[1]
                    return
            messagebox.showinfo("Buscar", "Producto no encontrado")
            limpiar()

    def actualizar():
        global nombre_original
        producto = txt_producto.get().strip()
        precio = txt_precio.get().strip()
        cantidad = txt_cantidad.get().strip()
        categoria = txt_categoria.get().strip()

        errores = []
        if not nombre_original:
            errores.append("Busca un producto antes de modificar")
        if not producto:
            errores.append("El producto no puede estar vacío")
        if not precio.isnumeric():
            errores.append("El precio debe ser numérico")
        if not cantidad.isnumeric():
            errores.append("La cantidad debe ser numérica")
        if not categoria:
            errores.append("La categoría no puede estar vacía")

        if errores:
            messagebox.showerror("Error de validación", "\n".join(errores))
            return

        datos = {
            "anterior": nombre_original,
            "producto": producto,
            "precio": int(precio),
            "cantidad": int(cantidad),
            "categoria": categoria
        }

        res = update(datos)
        if res["respuesta"]:
            messagebox.showinfo("Éxito", res["mensaje"])
            llenar_tabla_productos()
            limpiar()
        else:
            messagebox.showerror("Error", res["mensaje"])

    def eliminar():
        id_producto = txt_id.get()
        if not id_producto:
            messagebox.showwarning("Error", "Busca un producto antes de eliminar")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este producto?"):
            res = delete(int(id_producto))
            if res["respuesta"]:
                messagebox.showinfo("Éxito", res["mensaje"])
                llenar_tabla_productos()
                limpiar()
            else:
                messagebox.showerror("Error", res["mensaje"])

    # ==============================================
    # FUNCIONES PARA LA TABLA DE PRODUCTOS
    # ==============================================
    def llenar_tabla_productos(columna=None, ascendente=True):
        tabla_productos.delete(*tabla_productos.get_children())
        
        if columna is None:
            columna = orden_actual["columna"]
            ascendente = orden_actual["ascendente"]
        else:
            if columna == orden_actual["columna"]:
                ascendente = not orden_actual["ascendente"]
            else:
                ascendente = True
            orden_actual["columna"] = columna
            orden_actual["ascendente"] = ascendente
        
        if columna == "precio":
            orden = "precio ASC" if ascendente else "precio DESC"
        elif columna == "producto":
            orden = "producto ASC" if ascendente else "producto DESC"
        elif columna == "fecha":
            orden = "fecha ASC" if ascendente else "fecha DESC"
        elif columna == "cantidad":
            orden = "cantidad ASC" if ascendente else "cantidad DESC"
        elif columna == "categoria":
            orden = "categoria ASC" if ascendente else "categoria DESC"
        else:
            orden = "producto ASC"
        
        res = findAll(orden)
        productos = res.get("producto", [])
        
        for fila in productos:
            tabla_productos.insert("", END, values=fila)
        
        actualizar_encabezados_productos()
        actualizar_lista_productos()

    def actualizar_encabezados_productos():
        for col in tabla_productos['columns']:
            texto_original = {
                "id": "ID",
                "producto": "Producto",
                "precio": "Precio",
                "cantidad": "Cantidad",
                "categoria": "Categoría",
                "fecha": "Fecha"
            }[col]

            if col == orden_actual["columna"]:
                direccion = "↑" if orden_actual["ascendente"] else "↓"
                tabla_productos.heading(col, text=f"{texto_original} {direccion}")
            else:
                tabla_productos.heading(col, text=texto_original)

    def ordenar_por(columna):
        def handler():
            llenar_tabla_productos(columna)
        return handler

    def actualizar_lista_productos():
        res = findAll()
        productos = res.get("producto", [])
        nombres_productos = [p[1] for p in productos]
        e_producto_mov['values'] = nombres_productos

    def mostrar_bajo_stock():
        umbral = 5
        res = find_low_stock(umbral)
        productos = res.get("producto", [])
        
        if productos:
            tabla_productos.delete(*tabla_productos.get_children())
            for fila in productos:
                tabla_productos.insert("", END, values=fila)
            messagebox.showwarning("Bajo Stock", f"Hay {len(productos)} productos con menos de {umbral} unidades")
        else:
            messagebox.showinfo("Bajo Stock", "No hay productos con stock bajo")
            llenar_tabla_productos()

    def verificar_bajo_stock_inicio():
        umbral = 5
        res = find_low_stock(umbral)
        productos = res.get("producto", [])
        
        if productos:
            messagebox.showwarning("Bajo Stock al Inicio", 
                                 f"¡Atención! Hay {len(productos)} productos con menos de {umbral} unidades:\n\n" +
                                 "\n".join([f"- {p[1]} ({p[3]} unidades)" for p in productos]))

    # ==============================================
    # FUNCIONES PARA SUGERENCIAS DE BÚSQUEDA
    # ==============================================
    def mostrar_sugerencias(event):
        nonlocal sugerencias_listbox
        
        texto = txt_producto.get().strip()
        
        if not texto:
            if sugerencias_listbox:
                sugerencias_listbox.place_forget()
            return
        
        sugerencias = search_suggestions(texto)
        
        if not sugerencias:
            if sugerencias_listbox:
                sugerencias_listbox.place_forget()
            return
        
        if not sugerencias_listbox:
            sugerencias_listbox = Listbox(v, height=5, font=fuente, bg=COLOR_ENTRADA, fg=COLOR_FONDO)
            sugerencias_listbox.bind("<<ListboxSelect>>", seleccionar_sugerencia)
        
        sugerencias_listbox.delete(0, END)
        for sug in sugerencias:
            sugerencias_listbox.insert(END, sug[1])
        
        x = e_producto.winfo_x()
        y = e_producto.winfo_y() + e_producto.winfo_height()
        width = e_producto.winfo_width()
        
        sugerencias_listbox.place(x=x, y=y, width=width)
        sugerencias_listbox.lift()

    def seleccionar_sugerencia(event):
        nonlocal sugerencias_listbox, nombre_original
        
        if not sugerencias_listbox:
            return
        
        seleccion = sugerencias_listbox.curselection()
        if not seleccion:
            return
        
        producto_seleccionado = sugerencias_listbox.get(seleccion[0])
        
        res = findAll()
        productos = res.get("producto", [])
        for fila in productos:
            if fila[1] == producto_seleccionado:
                txt_id.set(fila[0])
                txt_producto.set(fila[1])
                txt_precio.set(fila[2])
                txt_cantidad.set(fila[3])
                txt_categoria.set(fila[4])
                nombre_original = fila[1]
                break
        
        sugerencias_listbox.place_forget()

    def ocultar_sugerencias(event):
        nonlocal sugerencias_listbox
        if sugerencias_listbox:
            sugerencias_listbox.place_forget()

    # ==============================================
    # FUNCIONES PARA MOVIMIENTOS DE INVENTARIO
    # ==============================================
    def cargar_movimientos_entrada():
        try:
            db = conexion.conectar()
            if db is None:
                print("Error: No se pudo conectar a la base de datos")
                return
                
            cursor = db.cursor()
            
            cursor.execute("""
                SELECT id, id_producto, producto, fecha, descripcion, cantidad, tipo 
                FROM entradas 
                ORDER BY fecha DESC
            """)
            
            movimientos = cursor.fetchall()
            
            tabla_entradas.delete(*tabla_entradas.get_children())
            for mov in movimientos:
                tabla_entradas.insert("", END, values=mov)
                
        except Exception as ex:
            print(f"Error al cargar movimientos de entrada: {str(ex)}")
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'db' in locals() and db is not None: db.close()

    def cargar_movimientos_salida():
        try:
            db = conexion.conectar()
            if db is None:
                print("Error: No se pudo conectar a la base de datos")
                return
                
            cursor = db.cursor()
            
            cursor.execute("""
                SELECT id, id_producto, producto, fecha, descripcion, cantidad, tipo 
                FROM salidas 
                ORDER BY fecha DESC
            """)
            
            movimientos = cursor.fetchall()
            
            tabla_salidas.delete(*tabla_salidas.get_children())
            for mov in movimientos:
                tabla_salidas.insert("", END, values=mov)
                
        except Exception as ex:
            print(f"Error al cargar movimientos de salida: {str(ex)}")
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'db' in locals() and db is not None: db.close()

    def registrar_movimiento():
        producto_mov = txt_descripcion.get().strip()
        if not producto_mov:
            messagebox.showerror("Error", "Debe seleccionar un producto")
            return
        res = findAll()
        productos = res.get("producto", [])
        producto_encontrado = None
        for p in productos:
            if p[1] == producto_mov:
                producto_encontrado = p
                break
        if not producto_encontrado:
            messagebox.showerror("Error", "Producto no encontrado en la base de datos")
            return
        txt_id.set(producto_encontrado[0])
        txt_producto.set(producto_encontrado[1])
        txt_precio.set(producto_encontrado[2])
        txt_cantidad.set(producto_encontrado[3])
        txt_categoria.set(producto_encontrado[4])
        nonlocal nombre_original
        nombre_original = producto_encontrado[1]
        cantidad_mov = txt_cantidad_movimiento.get().strip()
        tipo_movimiento = txt_tipo_movimiento.get()
        if not cantidad_mov.isnumeric() or int(cantidad_mov) <= 0:
            messagebox.showerror("Error", "La cantidad debe ser un número positivo")
            return
        cantidad_mov = int(cantidad_mov)
        cantidad_actual = int(txt_cantidad.get())
        if tipo_movimiento == "entrada":
            nueva_cantidad = cantidad_actual + cantidad_mov
        else:
            if cantidad_actual < cantidad_mov:
                messagebox.showerror("Error", "No hay suficiente stock para esta salida")
                return
            nueva_cantidad = cantidad_actual - cantidad_mov
        datos = {
            "anterior": nombre_original,
            "producto": txt_producto.get(),
            "precio": int(txt_precio.get()),
            "cantidad": nueva_cantidad,
            "categoria": txt_categoria.get()
        }
        res = update(datos)
        if not res["respuesta"]:
            messagebox.showerror("Error", f"No se pudo actualizar el stock: {res['mensaje']}")
            return
        try:
            db = conexion.conectar()
            if db is None:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos")
                return
            cursor = db.cursor()
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Distinción en la descripción
            descripcion_usuario = f"{usuario} (ADMIN)" if tipo_usuario == "admin" else usuario
            if tipo_movimiento == "entrada":
                sql = """
                INSERT INTO entradas (id_producto, producto, fecha, descripcion, cantidad, tipo)
                VALUES (?, ?, ?, ?, ?, ?)
                """
            else:
                sql = """
                INSERT INTO salidas (id_producto, producto, fecha, descripcion, cantidad, tipo)
                VALUES (?, ?, ?, ?, ?, ?)
                """
            valores = (
                txt_id.get(),
                txt_producto.get(),
                fecha_actual,
                descripcion_usuario,
                cantidad_mov,
                tipo_movimiento.upper()
            )
            cursor.execute(sql, valores)
            db.commit()
            if tipo_movimiento == "entrada":
                cargar_movimientos_entrada()
            else:
                cargar_movimientos_salida()
            txt_cantidad.set(str(nueva_cantidad))
            messagebox.showinfo("Éxito", f"Movimiento de {tipo_movimiento} registrado y stock actualizado")
            limpiar_campos_movimiento()
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo registrar el movimiento: {str(ex)}")
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'db' in locals() and db is not None: db.close()

    def limpiar_campos_movimiento():
        txt_descripcion.set("")
        txt_cantidad_movimiento.set("1")
        txt_tipo_movimiento.set("entrada")

    def incrementar_cantidad():
        current = int(txt_cantidad_movimiento.get())
        txt_cantidad_movimiento.set(str(current + 1))

    def decrementar_cantidad():
        current = int(txt_cantidad_movimiento.get())
        if current > 1:
            txt_cantidad_movimiento.set(str(current - 1))

    def bloquear_reordenamiento_columnas(event):
        region = tabla_productos.identify_region(event.x, event.y)
        if region == "separator":  # Esto evita que se muevan o redimensionen columnas
            return "break"
    
    def bloquear_scroll_horizontal(event):
        """Bloquea el scroll horizontal en todas las tablas"""
        return "break"

    def forzar_foco_entry(event, entry_widget):
        """Fuerza el foco en un campo de entrada"""
        entry_widget.focus_set()
        entry_widget.icursor(tk.END)  # Coloca el cursor al final
        return "break"

    # ==============================================
    # INTERFAZ GRÁFICA MODERNIZADA
    # ==============================================

    # Frame principal con padding
    main_frame = ttk.Frame(v)
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # Frame de productos con estilo moderno
    frame_productos = ttk.LabelFrame(main_frame, text="Gestión de Productos", padding=(15, 10))
    frame_productos.grid(row=0, column=0, sticky="nsew", pady=(0, 15))

    # Grid configuration para expansión
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=0)
    main_frame.rowconfigure(1, weight=1)

    # Controles de productos en grid organizado
    controls_frame = ttk.Frame(frame_productos)
    controls_frame.pack(fill=X, expand=True, pady=5)

    # Campos de entrada con etiquetas
    fields = [
        ("Producto", txt_producto, 30),
        ("Precio", txt_precio, 30),
        ("Cantidad", txt_cantidad, 30),
        ("Categoría", txt_categoria, 30)
    ]

    entries_productos = []
    for i, (text, var, width) in enumerate(fields):
        ttk.Label(controls_frame, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entry = ttk.Entry(controls_frame, textvariable=var, width=width)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
        entries_productos.append(entry)
        
        # Configurar el campo para responder correctamente
        entry.bind("<Button-1>", lambda e, ent=entry: forzar_foco_entry(e, ent))
        entry.bind("<FocusIn>", lambda e, ent=entry: ent.select_range(0, tk.END))
        
        if text == "Producto":
            e_producto = entry
            e_producto.bind("<KeyRelease>", mostrar_sugerencias)
            e_producto.bind("<FocusOut>", ocultar_sugerencias)
    
    # Deshabilitar campos de productos si es usuario
    if tipo_usuario == "usuario":
        for entry in entries_productos:
            entry.config(state="disabled")

    # Botones con mejor espaciado
    buttons_frame = ttk.Frame(frame_productos)
    buttons_frame.pack(fill=X, expand=True, pady=(10, 0))

    button_data = [
        ("Guardar", guardar),
        ("Modificar", actualizar),
        ("Eliminar", eliminar),
        ("Limpiar", limpiar)
        
    ]

    botones_productos = []
    for i, (text, command) in enumerate(button_data):
        btn = ttk.Button(buttons_frame, text=text, command=command)
        btn.grid(row=0, column=i, padx=5, pady=5)
        botones_productos.append(btn)
    
    # Deshabilitar funciones de administración si es usuario
    if tipo_usuario == "usuario":
        for btn in botones_productos[:3]:  # Guardar, Modificar, Eliminar
            btn.config(state="disabled")

    # Tabla de productos con scrollbar
    table_frame = ttk.Frame(frame_productos)
    table_frame.pack(fill=BOTH, expand=True, pady=(10, 0))

    # Scrollbar vertical
    scroll_y = ttk.Scrollbar(table_frame)
    scroll_y.pack(side=RIGHT, fill=Y)

    tabla_productos = ttk.Treeview(table_frame, height=8, yscrollcommand=scroll_y.set)
    tabla_productos.bind("<Button-1>", bloquear_reordenamiento_columnas)
    tabla_productos.bind("<MouseWheel>", bloquear_scroll_horizontal)
    tabla_productos.bind("<Shift-MouseWheel>", bloquear_scroll_horizontal)
    tabla_productos.bind("<Control-MouseWheel>", bloquear_scroll_horizontal)

    tabla_productos.pack(fill=BOTH, expand=True)

    scroll_y.config(command=tabla_productos.yview)

    # Configuración de columnas
    tabla_productos['columns'] = ("id", "producto", "precio", "cantidad", "categoria", "fecha")

    tabla_productos.column("#0", width=0, stretch=NO)
    tabla_productos.column("id", width=0, stretch=NO)
    tabla_productos.column("producto", anchor=W, width=200)
    tabla_productos.column("precio", anchor=CENTER, width=100)
    tabla_productos.column("cantidad", anchor=CENTER, width=100)
    tabla_productos.column("categoria", anchor=W, width=150)
    tabla_productos.column("fecha", anchor=CENTER, width=120)

    # Encabezados con funciones de ordenación
    for col, text in [("producto", "Producto"), ("precio", "Precio"), 
                      ("cantidad", "Cantidad"), ("categoria", "Categoría"), 
                      ("fecha", "Fecha")]:
        tabla_productos.heading(col, text=text, anchor=CENTER, 
                              command=ordenar_por(col))

    # Frame de movimientos
    frame_movimientos = ttk.LabelFrame(main_frame, text="Registro de Movimientos de Inventario", padding=(15, 10))
    frame_movimientos.grid(row=1, column=0, sticky="nsew", pady=(0, 10))

    # Configuración de grid para expansión
    frame_movimientos.columnconfigure(0, weight=1)
    frame_movimientos.columnconfigure(1, weight=1)
    frame_movimientos.rowconfigure(1, weight=1)

    # Controles para movimientos
    mov_controls_frame = ttk.Frame(frame_movimientos)
    mov_controls_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

    # Campos de movimiento
    ttk.Label(mov_controls_frame, text="Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    e_producto_mov = ttk.Combobox(mov_controls_frame, textvariable=txt_descripcion, width=40)
    e_producto_mov.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(mov_controls_frame, text="Tipo:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    opciones_tipo = ttk.Combobox(mov_controls_frame, textvariable=txt_tipo_movimiento, 
                                values=["entrada", "salida"], state="readonly", width=10)
    opciones_tipo.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    ttk.Label(mov_controls_frame, text="Cantidad:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
    frame_cantidad = ttk.Frame(mov_controls_frame)
    frame_cantidad.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    btn_decrementar = ttk.Button(frame_cantidad, text="-", width=3, command=decrementar_cantidad)
    btn_decrementar.pack(side=LEFT)

    e_cantidad_mov = ttk.Entry(frame_cantidad, textvariable=txt_cantidad_movimiento, width=5)
    e_cantidad_mov.pack(side=LEFT, padx=5)

    btn_incrementar = ttk.Button(frame_cantidad, text="+", width=3, command=incrementar_cantidad)
    btn_incrementar.pack(side=LEFT)

    # Botón de registrar movimiento
    ttk.Button(mov_controls_frame, text="Registrar Movimiento", command=registrar_movimiento).grid(
        row=0, column=6, padx=10, pady=5, sticky="e")

    # Tablas de entradas y salidas
    tablas_frame = ttk.Frame(frame_movimientos)

    tablas_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

    # Frame para entradas
    frame_entradas = ttk.LabelFrame(tablas_frame, text="Entradas", padding=(10, 5))
    frame_entradas.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))

    # Scrollbar para entradas
    scroll_entradas_y = ttk.Scrollbar(frame_entradas)
    scroll_entradas_y.pack(side=RIGHT, fill=Y)

    tabla_entradas = ttk.Treeview(frame_entradas, height=10, yscrollcommand=scroll_entradas_y.set)
    tabla_entradas.bind("<Button-1>", bloquear_reordenamiento_columnas)
    tabla_entradas.bind("<MouseWheel>", bloquear_scroll_horizontal)
    tabla_entradas.bind("<Shift-MouseWheel>", bloquear_scroll_horizontal)
    tabla_entradas.bind("<Control-MouseWheel>", bloquear_scroll_horizontal)
    tabla_entradas.pack(fill=BOTH, expand=True)

    scroll_entradas_y.config(command=tabla_entradas.yview)

    # Configuración de columnas para entradas
    tabla_entradas['columns'] = ("id", "id_producto", "producto", "fecha", "descripcion", "cantidad", "tipo")

    tabla_entradas.column("#0", width=0, stretch=NO)
    tabla_entradas.column("id", width=0, stretch=NO)
    tabla_entradas.column("id_producto", width=0, stretch=NO)
    tabla_entradas.column("producto", width=150, minwidth=150, stretch=NO, anchor=W)
    tabla_entradas.column("fecha", width=120, minwidth=120, stretch=NO, anchor=CENTER)
    tabla_entradas.column("descripcion", width=150, minwidth=150, stretch=NO, anchor=W)
    tabla_entradas.column("cantidad", width=80, minwidth=80, stretch=NO, anchor=CENTER)
    tabla_entradas.column("tipo", width=80, minwidth=80, stretch=YES, anchor=CENTER)  # Esta columna se expandirá

    # Encabezados
    for col, text in [("producto", "Producto"), ("fecha", "Fecha"), ("descripcion", "Descripción"), 
                      ("cantidad", "Cantidad"), ("tipo", "Tipo")]:
        tabla_entradas.heading(col, text=text, anchor=CENTER)

    # Frame para salidas
    frame_salidas = ttk.LabelFrame(tablas_frame, text="Salidas", padding=(10, 5))
    frame_salidas.pack(side=RIGHT, fill=BOTH, expand=True, padx=(5, 0))

    # Scrollbar para salidas
    scroll_salidas_y = ttk.Scrollbar(frame_salidas)
    scroll_salidas_y.pack(side=RIGHT, fill=Y)

    tabla_salidas = ttk.Treeview(frame_salidas, height=10, yscrollcommand=scroll_salidas_y.set)
    tabla_salidas.bind("<Button-1>", bloquear_reordenamiento_columnas)
    tabla_salidas.bind("<MouseWheel>", bloquear_scroll_horizontal)
    tabla_salidas.bind("<Shift-MouseWheel>", bloquear_scroll_horizontal)
    tabla_salidas.bind("<Control-MouseWheel>", bloquear_scroll_horizontal)
    tabla_salidas.pack(fill=BOTH, expand=True)

    scroll_salidas_y.config(command=tabla_salidas.yview)

    # Configuración de columnas para salidas (igual que entradas)
    tabla_salidas['columns'] = ("id", "id_producto", "producto", "fecha", "descripcion", "cantidad", "tipo")

    tabla_salidas.column("#0", width=0, stretch=NO)
    tabla_salidas.column("id", width=0, stretch=NO)
    tabla_salidas.column("id_producto", width=0, stretch=NO)
    tabla_salidas.column("producto", width=150, minwidth=150, stretch=NO, anchor=W)
    tabla_salidas.column("fecha", width=120, minwidth=120, stretch=NO, anchor=CENTER)
    tabla_salidas.column("descripcion", width=150, minwidth=150, stretch=NO, anchor=W)
    tabla_salidas.column("cantidad", width=80, minwidth=80, stretch=NO, anchor=CENTER)
    tabla_salidas.column("tipo", width=80, minwidth=80, stretch=YES, anchor=CENTER)  # Esta columna se expandirá

    # Encabezados (igual que entradas)
    for col, text in [("producto", "Producto"), ("fecha", "Fecha"), ("descripcion", "Descripción"), 
                      ("cantidad", "Cantidad"), ("tipo", "Tipo")]:
        tabla_salidas.heading(col, text=text, anchor=CENTER)

    # ==============================================
    # MENÚ PRINCIPAL MODERNIZADO
    # ==============================================
    menu_top = Menu(v, tearoff=0, bg=COLOR_FONDO_SECUNDARIO, fg=COLOR_TEXTO, 
                   activebackground=COLOR_BOTONES, activeforeground=COLOR_TEXTO)
    v.config(menu=menu_top)

    # Menú Archivo
    menu_archivo = Menu(menu_top, tearoff=0)
    menu_archivo.add_command(label="Salir", command=salir)
    menu_top.add_cascade(label="Archivo", menu=menu_archivo)

    # Menú Ordenar
    menu_orden = Menu(menu_top, tearoff=0)
    menu_orden.add_command(label="Producto (A-Z)", command=ordenar_por("producto"))
    menu_orden.add_command(label="Precio (↑)", command=ordenar_por("precio"))
    menu_orden.add_command(label="Precio (↓)", command=lambda: llenar_tabla_productos("precio", False))
    menu_orden.add_command(label="Fecha (↑)", command=ordenar_por("fecha"))
    menu_orden.add_command(label="Fecha (↓)", command=lambda: llenar_tabla_productos("fecha", False))
    menu_orden.add_command(label="Cantidad (↑)", command=ordenar_por("cantidad"))
    menu_orden.add_command(label="Cantidad (↓)", command=lambda: llenar_tabla_productos("cantidad", False))
    menu_top.add_cascade(label="Ordenar", menu=menu_orden)
    
    # Deshabilitar menú de ordenar si es usuario
    if tipo_usuario == "usuario":
        menu_orden.entryconfig("Producto (A-Z)", state="disabled")
        menu_orden.entryconfig("Precio (↑)", state="disabled")
        menu_orden.entryconfig("Precio (↓)", state="disabled")
        menu_orden.entryconfig("Fecha (↑)", state="disabled")
        menu_orden.entryconfig("Fecha (↓)", state="disabled")
        menu_orden.entryconfig("Cantidad (↑)", state="disabled")
        menu_orden.entryconfig("Cantidad (↓)", state="disabled")

    # ==============================================
    # INICIAR APLICACIÓN
    # ==============================================
    llenar_tabla_productos()
    cargar_movimientos_entrada()
    cargar_movimientos_salida()
    verificar_bajo_stock_inicio()
    actualizar_lista_productos()

    # Establecer foco en el campo de producto después de que la ventana esté lista
    def establecer_foco_inicial():
        if tipo_usuario == "admin":
            e_producto.focus_set()
            e_producto.icursor(tk.END)
        v.lift()  # Traer la ventana al frente
        v.focus_force()  # Forzar el foco en la ventana

    v.after(200, establecer_foco_inicial)

    v.mainloop()



# Iniciar el proceso de login
if __name__ == "__main__":
    mostrar_login()