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

            self.pantalla_actual.actualizar_datos(datos['texto_a_mostrar'], datos['resultados'])

        self.pantalla_actual.pack(fill="both", expand=True)

    def mostrar_bienvenida(self):
        self.cambiar_pantalla(PantallaBienvenida)

    def iniciar_analisis(self, texto_crudo, texto_limpio):

        resultados_simulados = {
            "Variables": [0, "Pendiente de implementar"],
            "Palabras Res.": [0, "Pendiente de implementar"],
            "Números Enteros": [0, "Pendiente de implementar"],
            "Números Reales": [0, "Pendiente de implementar"],
            "Operadores": [0, "Pendiente de implementar"],
        }

        datos_paquete = {
            'texto_a_mostrar': texto_limpio,
            'resultados': resultados_simulados
        }

        self.cambiar_pantalla(PantallaResultados, datos=datos_paquete)