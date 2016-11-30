'''
Función codificar
Palabra: String a codificar
Avance: int posiciones que avanza en el alfabeto
'''
def Codificar(Palabra, Avance):
    Clave = ''
    Tope = len(alfabetoMayus)
    Posicion = 0
    for letra in Palabra:
        for i in range(Tope):
            if (i + Avance < Tope):
                Posicion = i + Avance
            else:
                Posicion = abs((Tope - i) - Avance)
            if letra == alfabetoMinus[i]:
                Clave = Clave + alfabetoMinus[Posicion]
            elif letra == alfabetoMayus[i]:
                Clave = Clave + alfabetoMayus[Posicion]
    return Clave

#***************************************
Clave = Codificar("Hola", 3)
print(Clave)
