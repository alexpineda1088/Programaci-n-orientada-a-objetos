class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "estas muerto")

    def daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class Luchador(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) flecha de Acero , daño 8. (2) hielo , daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


class Arquero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arco = arco

    def atributos(self):
        super().atributos()
        print("·Arco:", self.arco)

    def daño(self, enemigo):
        return (self.fuerza + self.inteligencia) * self.arco - enemigo.defensa


class Hechicero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, varita):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.varita = varita

    def atributos(self):
        super().atributos()
        print("·Varita:", self.varita)

    def daño(self, enemigo):
        return (self.inteligencia * 2) * self.varita - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1 = Luchador("Alex", 30, 11, 6, 90, 8)
personaje_2 = Hechicero("Daniel", 9, 13, 2, 70, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)