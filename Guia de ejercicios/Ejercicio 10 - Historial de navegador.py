class HistorialdeNavegacion:
    def __init__(self):
        self.pila = []
        self.paginaactual = None
        
    def visitarpagina(self, pagina):
        if self.paginaactual:
            self.pila.append(self.paginaactual)
        self.paginaactual = pagina
        print(f"Visitando: {pagina}")
        
    def ir_hacia_atras(self):
        if self.pila:
            self.paginaactual = self.pila.pop()
            print(f"Volviendo a {self.paginaactual}")
        else:
            print("No hay paginas en el historial para ir hacia atras.")
    
    def mostrar_pagina_actual(self):
        if self.paginaactual:
            print(f"Pagina actual: {self.paginaactual}")
        else:
            print("No hay ninguna pagina abierta.")
    
    
historial = HistorialdeNavegacion()

historial.visitarpagina("Pagina1.com")
historial.visitarpagina("Pagina2.com")
historial.visitarpagina("Pagina3.com")

historial.mostrar_pagina_actual()

historial.ir_hacia_atras()
historial.mostrar_pagina_actual()

historial.ir_hacia_atras()
historial.mostrar_pagina_actual()

historial.ir_hacia_atras()
historial.mostrar_pagina_actual()

historial.ir_hacia_atras()