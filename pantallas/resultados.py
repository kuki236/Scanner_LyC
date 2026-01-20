import tkinter as tk
from tkinter import ttk

class PantallaResultados(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # --- COLORES (Misma paleta que Bienvenida) ---
        self.color_fondo = "#0f111a"      # Negro azulado
        self.color_panel = "#161b22"      # Gris oscuro para paneles
        self.color_acento = "#00f0ff"     # Cian brillante
        self.color_texto = "#e6edf3"      # Blanco suave
        self.color_borde = "#30363d"      # Gris borde
        
        self.configure(bg=self.color_fondo)

        # --- TÍTULO SUPERIOR ---
        header_frame = tk.Frame(self, bg=self.color_fondo)
        header_frame.pack(fill="x", padx=20, pady=(15, 10))
        
        lbl_titulo = tk.Label(
            header_frame, 
            text="ANÁLISIS LÉXICO FINALIZADO", 
            font=("Helvetica", 14, "bold"),
            bg=self.color_fondo, 
            fg=self.color_acento
        )
        lbl_titulo.pack(side="left")
        
        btn_volver = tk.Button(
            header_frame,
            text="← VOLVER",
            font=("Helvetica", 9, "bold"),
            bg="#21262d",
            fg=self.color_texto,
            relief="flat",
            cursor="hand2",
            command=lambda: controller.mostrar_bienvenida() # Asumiendo que tienes este método
        )
        btn_volver.pack(side="right")

        # --- DIVISIÓN DE PANTALLA (PANED WINDOW) ---
        # Esto crea la división deslizable entre Izq y Der
        self.paned = tk.PanedWindow(
            self, 
            orient="horizontal", 
            bg=self.color_fondo, 
            sashwidth=4,
            sashrelief="flat"
        )
        self.paned.pack(fill="both", expand=True, padx=20, pady=10)

        # ==========================================
        # ⬅️ LADO IZQUIERDO: TEXTO CRUDO
        # ==========================================
        frame_izq = tk.Frame(self.paned, bg=self.color_panel)
        self.paned.add(frame_izq, minsize=300) # Panel izquierdo añadido

        # Etiqueta "Código Fuente"
        tk.Label(frame_izq, text=" CÓDIGO FUENTE (CRUDO)", font=("Consolas", 10, "bold"), bg=self.color_panel, fg="#8b9bb4", anchor="w").pack(fill="x", padx=10, pady=5)

        # Widget de Texto (Scrollable)
        self.text_area = tk.Text(
            frame_izq, 
            bg="#0d1117", 
            fg="#c9d1d9", 
            font=("Consolas", 11), 
            relief="flat",
            padx=10, pady=10,
            insertbackground="white" # Cursor blanco
        )
        self.text_area.pack(fill="both", expand=True, padx=2, pady=2)

        # ==========================================
        # ➡️ LADO DERECHO: TABLA DE RESULTADOS
        # ==========================================
        frame_der = tk.Frame(self.paned, bg=self.color_fondo)
        self.paned.add(frame_der, minsize=400) # Panel derecho añadido

        tk.Label(frame_der, text=" TABLA DE SÍMBOLOS", font=("Consolas", 10, "bold"), bg=self.color_fondo, fg="#8b9bb4", anchor="w").pack(fill="x", padx=10, pady=5)

        # Contenedor para la tabla (Canvas + Scrollbar por si hay muchos resultados)
        self.canvas_tabla = tk.Canvas(frame_der, bg=self.color_fondo, highlightthickness=0)
        scrollbar_tabla = tk.Scrollbar(frame_der, orient="vertical", command=self.canvas_tabla.yview)
        self.scrollable_frame = tk.Frame(self.canvas_tabla, bg=self.color_fondo)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_tabla.configure(scrollregion=self.canvas_tabla.bbox("all"))
        )

        self.canvas_tabla.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_tabla.configure(yscrollcommand=scrollbar_tabla.set)

        self.canvas_tabla.pack(side="left", fill="both", expand=True)
        scrollbar_tabla.pack(side="right", fill="y")

        # --- ENCABEZADOS DE LA TABLA ---
        # Estructura: [ Categoría (Ancho fijo) | Cant (Ancho fijo) | Detalle (Expandible) ]
        self.crear_fila_tabla("CATEGORÍA", "CANT.", "DETALLE (Tokens encontrados)", es_header=True)

    def crear_fila_tabla(self, categoria, cantidad, detalle, es_header=False):
        """
        Crea una fila visual estilo 'Grid' manual para parecerse al cuaderno.
        """
        if es_header:
            bg_color = "#21262d"
            fg_color = self.color_acento
            font_style = ("Helvetica", 10, "bold")
        else:
            bg_color = self.color_fondo
            fg_color = self.color_texto
            font_style = ("Consolas", 10)

        # Contenedor de la fila
        fila = tk.Frame(self.scrollable_frame, bg=bg_color, pady=2)
        fila.pack(fill="x", expand=True, pady=1)

        # 1. Columna Categoría (Ancho fijo aprox)
        lbl_cat = tk.Label(fila, text=categoria, width=18, anchor="w", bg=bg_color, fg=fg_color, font=font_style)
        lbl_cat.pack(side="left", padx=5)

        # Separador visual
        tk.Label(fila, text="|", bg=bg_color, fg="#30363d").pack(side="left")

        # 2. Columna Cantidad (Centrado)
        lbl_cant = tk.Label(fila, text=str(cantidad), width=6, anchor="center", bg=bg_color, fg=fg_color, font=font_style)
        lbl_cant.pack(side="left", padx=5)

        # Separador visual
        tk.Label(fila, text="|", bg=bg_color, fg="#30363d").pack(side="left")

        # 3. Columna Detalle (Se expande y hace wrap)
        # Usamos Message o Label con wraplength para que el texto baje si es muy largo
        lbl_det = tk.Label(
            fila, 
            text=detalle, 
            anchor="w", 
            justify="left",
            bg=bg_color, 
            fg=fg_color, 
            font=font_style,
            wraplength=350  # Ajustar según ancho pantalla
        )
        lbl_det.pack(side="left", fill="x", expand=True, padx=5)
        
        # Línea divisoria inferior
        if not es_header:
            tk.Frame(self.scrollable_frame, height=1, bg="#21262d").pack(fill="x")

    def actualizar_datos(self, texto_crudo, resultados_diccionario):
        """
        Método que llamará el controlador para llenar la pantalla.
        """
        # 1. Llenar el texto crudo a la izquierda
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", texto_crudo)
        
        # 2. Limpiar tabla derecha (menos el header)
        # (Aquí podrías implementar lógica para borrar widgets viejos si se reusa la pantalla)
        
        # 3. Llenar filas según el diccionario de resultados
        # Se espera un dict: {"Variables": [6, "a, b, c"], "Enteros": [2, "10, 20"]...}
        for clave, valor in resultados_diccionario.items():
            # valor[0] es cantidad, valor[1] es el string detalle
            self.crear_fila_tabla(clave, valor[0], valor[1])