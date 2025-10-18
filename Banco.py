class Clinica:
    def __init__(self, lista_personas):
        self.personas = lista_personas
        self.urgencias = []
        self.con_cita = []
        self.sin_cita = []
        self.limite_urgencias = 3  # máximo permitido

    def clasificar(self, lista=None):
        if lista is None:
            lista = self.personas

        if not lista:  # Caso base: lista vacía
            return

        nombre, tipo = lista[0]

        if tipo == "urgencia":
            if len(self.urgencias) < self.limite_urgencias:
                self.urgencias.append((nombre, tipo))
            else:
                print(f"⚠️ Ya hay 3 urgencias. {nombre} no se puede registrar como urgencia.")
                self.sin_cita.append((nombre, "sin_cita"))  # lo tratamos como sin cita
        elif tipo == "cita":
            self.con_cita.append((nombre, tipo))
        else:
            self.sin_cita.append((nombre, tipo))

        # Llamada recursiva con el resto de la lista
        self.clasificar(lista[1:])

    def mostrar_orden(self):
        orden = self.urgencias + self.con_cita + self.sin_cita
        print("\n📋 Orden de atención:")
        for nombre, tipo in orden:
            print(f"{nombre} - {tipo}")
