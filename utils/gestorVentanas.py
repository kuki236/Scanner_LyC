from pantallas.bienvenida import PantallaBienvenida
from pantallas.resultados import PantallaResultados  


class GestorVentanas:
    def __init__(self, root):
        self.root = root
        self.pantalla_actual = None
        self.escenarios = {}

    def cambiar_pantalla(self, nueva_pantalla_class, datos=None):
        if self.pantalla_actual:
            self.pantalla_actual.destroy()

        self.pantalla_actual = nueva_pantalla_class(self.root, self)
        
        if datos and hasattr(self.pantalla_actual, 'actualizar_datos'):

            self.pantalla_actual.actualizar_datos(datos['texto_crudo'], datos['resultados'])

        self.pantalla_actual.pack(fill="both", expand=True)

    def mostrar_bienvenida(self):
        self.cambiar_pantalla(PantallaBienvenida)

    def iniciar_analisis(self, texto_crudo, texto_limpio):

        resultados_simulados = {
            "Variables": [0, "Pendiente de implementar"],
            "Palabras Res.": [0, "Pendiente de implementar"],
            "Números": [0, "Pendiente de implementar"],
            "Operadores": [0, "Pendiente de implementar"],
            "Comentarios": [1, "Texto limpio generado"] # Solo para debug
        }

        datos_paquete = {
            'texto_crudo': texto_crudo,
            'resultados': resultados_simulados
        }

        self.cambiar_pantalla(PantallaResultados, datos=datos_paquete)