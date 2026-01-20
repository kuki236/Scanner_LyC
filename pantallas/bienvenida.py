import tkinter as tk
from tkinter import filedialog, messagebox
from logica.scanner import ScannerManual

class PantallaBienvenida(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.scanner = ScannerManual()
        self.color_fondo = "#0f111a"    
        self.color_acento = "#00f0ff"     
        self.color_texto = "#ffffff"      
        self.color_texto_gris = "#8b9bb4" 
        self.color_caja = "#161b22"       
        
        self.configure(bg=self.color_fondo)

        main_frame = tk.Frame(self, bg=self.color_fondo)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        lbl_titulo = tk.Label(
            main_frame, 
            text="Extracción de simbolos", 
            font=("Helvetica", 24, "bold"),
            bg=self.color_fondo, 
            fg=self.color_texto
        )
        lbl_titulo.pack(pady=(40, 0))

        lbl_subtitulo = tk.Label(
            main_frame, 
            text="BizaScanner", 
            font=("Helvetica", 30, "bold"),
            bg=self.color_fondo, 
            fg=self.color_acento
        )
        lbl_subtitulo.pack(pady=(0, 20))

        lbl_desc = tk.Label(
            main_frame, 
            text="Analiza archivos C y obtén un análisis detallado de sus símbolos.",
            font=("Segoe UI", 10),
            bg=self.color_fondo, 
            fg=self.color_texto_gris,
            justify="center"
        )
        lbl_desc.pack(pady=(0, 30))

        self.canvas_drop = tk.Canvas(
            main_frame, 
            width=500, 
            height=300, 
            bg=self.color_caja, 
            highlightthickness=0
        )
        self.canvas_drop.pack()

        self.rect_borde = self.canvas_drop.create_rectangle(
            10, 10, 490, 290, 
            outline="#2d3b4e", 
            width=2, 
            dash=(10, 10) 
        )

        self.canvas_drop.create_text(
            250, 100, 
            text="☁", 
            font=("Segoe UI Emoji", 40), 
            fill=self.color_texto_gris
        )

        self.canvas_drop.create_text(
            250, 160, 
            text="Carga tu archivo .C aquí", 
            font=("Helvetica", 14, "bold"), 
            fill=self.color_texto
        )
        


        self.btn_cargar = tk.Button(
            self.canvas_drop, 
            text="📂  CARGAR ARCHIVO", 
            font=("Helvetica", 10, "bold"),
            bg=self.color_acento, 
            fg="#000000",       
            activebackground="#ffffff",
            activeforeground="#000000",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            command=self.seleccionar_archivo
        )
        self.canvas_drop.create_window(250, 240, window=self.btn_cargar)

    def seleccionar_archivo(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar código fuente",
            filetypes=(("Archivos C", "*.c"),("Archivos C++", "*.cpp"), ("Archivos de texto", "*.txt"), ("Todos", "*.*"))
        )
        
        if ruta_archivo:
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    texto_crudo = f.read()

                # 2. Imprimimos en consola (Requisito)
                print("\n" + "="*40)
                print(f"CONTENIDO ORIGINAL DEL ARCHIVO ({ruta_archivo}):")
                print("="*40)
                print(texto_crudo)
                print("="*40 + "\n")

                # Aquí más adelante llamarás a la lógica de P2, P3 y P4
                # self.controller.iniciar_analisis(texto_crudo)
                texto_sin_comentarios = self.scanner.limpiar_comentarios(texto_crudo)
                print("\n" + ">"*20 + " TEXTO PROCESADO (SIN COMENTARIOS) " + "<"*20)
                print(texto_sin_comentarios)
                print("\n--------------------------------------------------")
                if self.controller:
                    self.controller.iniciar_analisis(texto_crudo, texto_sin_comentarios)
                else:
                    print("Error: No hay controlador asignado")

            except Exception as e:
                print(f"Error crítico leyendo el archivo: {e}")
                messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")