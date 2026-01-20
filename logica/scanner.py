class ScannerManual:
    def __init__(self):
        self.fuente = ""      
        self.pos = 0         
        self.longitud = 0

    def limpiar_comentarios(self, texto_entrada):
        self.fuente = texto_entrada
        self.longitud = len(texto_entrada)
        self.pos = 0
        texto_limpio = ""

        while self.pos < self.longitud:
            char_actual = self.fuente[self.pos]

            if char_actual == '/' and self.pos + 1 < self.longitud:
                siguiente_char = self.fuente[self.pos + 1]

                # --- CASO 1: Comentario de línea (//) ---
                if siguiente_char == '/':
                    self.pos += 2  
                    while self.pos < self.longitud and self.fuente[self.pos] != '\n':
                        self.pos += 1
                    continue 

                # --- CASO 2: Comentario de bloque (/* ... */) ---
                elif siguiente_char == '*':
                    self.pos += 2  
                    while self.pos < self.longitud - 1:
                        if self.fuente[self.pos] == '*' and self.fuente[self.pos + 1] == '/':
                            self.pos += 2  
                            break
                        self.pos += 1
                    continue

            texto_limpio += char_actual
            self.pos += 1

        return texto_limpio
    
def analizar(self, texto_a_analizar):
        self.fuente = texto_a_analizar
        self.longitud = len(texto_a_analizar)
        self.pos = 0
        
        # Diccionario para llenar la tabla
        encontrados = {
            "Variables": [],      
            "Palabras Res.": [],  
            "Números Enteros": [], 
            "Números Reales": [],  
            "Operadores": []      
        }

        while self.pos < self.longitud:
            char_actual = self.fuente[self.pos]

            # 1. Ignorar espacios en blanco (equivalente a tu while == ' ')
            if char_actual == ' ' or char_actual == '\t' or char_actual == '\n':
                # [LOGICA: Aumentar PosActual y continue]
                self.pos += 1
                continue

            # 2. Si es una letra (Inicio de Identificador o Palabra Reservada)
            # Equivalente a: IN ['a' .. 'z']
            elif ('a' <= char_actual <= 'z') or ('A' <= char_actual <= 'Z'):
                # [LOGICA: Bucle while mientras sea letra o digito]
                # [LOGICA: Verificar si es PR o ID]
                pass

            # 3. Si es un dígito (Inicio de Número Entero o Real)
            # Equivalente a: IN ['0' .. '9']
            elif '0' <= char_actual <= '9':
                # [LOGICA: Bucle while mientras sea digito]
                # [LOGICA: Chequear si aparece un punto '.' para Números Reales]
                pass

            # 4. Operadores de 1 caracter
            # Equivalente a: IN ['+', '-', '*', '/'] (y otros símbolos)
            elif char_actual in "+-*/=<>!&|%(){}[];,":
                # [LOGICA: Guardar token y avanzar]
                pass

            # 5. Error Lexicográfico
            else:
                # [LOGICA: Manejo de error o ignorar]
                self.pos += 1

        # Retorno de datos
        return {
            "Variables": [len(encontrados["Variables"]), ", ".join(encontrados["Variables"])],
            "Palabras Res.": [len(encontrados["Palabras Res."]), ", ".join(encontrados["Palabras Res."])],
            "Números Enteros": [len(encontrados["Números Enteros"]), ", ".join(encontrados["Números Enteros"])],
            "Números Reales": [len(encontrados["Números Reales"]), ", ".join(encontrados["Números Reales"])],
            "Operadores": [len(encontrados["Operadores"]), " ".join(encontrados["Operadores"])]
        }

# =============================================================================
# UBICACIÓN DEL ARCHIVO:
# Este código va dentro de la clase ScannerManual en "logica/scanner.py".
#
# CONEXIÓN:
# En "utils/gestorVentanas.py", busca la función "iniciar_analisis" y
# llama a este método: 
#      resultados = self.scanner.analizar(texto_limpio)
# Luego envía 'resultados' a la pantalla.
# =============================================================================
    
    # CONEXIÓN:
# En "utils/gestorVentanas.py", busca la función "iniciar_analisis" y
# llama a este método: 
#      resultados = self.scanner.analizar(texto_limpio)
# Luego envía 'resultados' a la pantalla.