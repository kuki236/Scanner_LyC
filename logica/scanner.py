class ScannerManual:
    def __init__(self):
        self.fuente = ""      
        self.pos = 0         
        self.longitud = 0

    def limpiar_comentarios(self, texto_entrada):
        """
        Recorre el texto carácter por carácter.
        Si encuentra // salta hasta el final de línea.
        Si encuentra /* salta hasta */.
        """
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