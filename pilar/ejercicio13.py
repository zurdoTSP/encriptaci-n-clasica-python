
#!/usr/bin/python

debug = False

# Cifrado por sustitucion

def get_alphabet():
    #"""Devuelve una lista con mayusculas, minuscula, numeros y un espacio"""
    alphabet = []

    # mayusculas:65-90
    for i in range(65,91):
        alphabet.append(chr(i))

    # minusculas:97-122
    for i in range(97,123):
        alphabet.append(chr(i))

    # numeros
    for i in range(10):
        alphabet.append(str(i))

    # espacio
    #alphabet.append(" ")

    return alphabet


def get_index(index = 0, length = 0):
    #"""Devuelve un indice valido dentro de un rango, evitando desbordamiento"""

    min_index = 0           # indice minimo
    max_index = length - 1      # indice maximo = longitud - 1

    while True:

        # index excede el limite superior
        if index > max_index:
            index -= length

        # index es menor al limite inferior
        elif index < min_index:
            index += length

        # index es valido
        else:
            break

    return index




def crypt(message = "", key = 0):
    #"""Cifra un mensaje usando sustitucion"""

    crypted = ""            # mensaje cifrado

    alphabet = get_alphabet()   # alfabeto
    length = len(alphabet)      # longitud del alfabeto
    index = 0           # indice de la letra en el alfabeto

    for letter in message:

        # se obtiene el indice de letter dentro de alphabet, si existe
        try:
            index = alphabet.index(letter)  # indice dentro del alfabeto
        except:
            print "No existe %s en el alfabeto" % (letter,)
            continue


        # se obtiene la nueva posicion, evitando desbordamiento
        move = index + key      # nueva posicion
        move = get_index(move,length)

        # debug
        if debug:
            print "move %d"%(move,)

        crypted += alphabet[move]   # agrega la letra al mensaje cifrado

        #debug
        if debug:
            print "%s = %s" % (alphabet[index],alphabet[move])

    return crypted


def decrypt(message = "", key = 0):
    #"""Decifra un mensaje usando sustitucion"""

    decrypted = ""          # mensaje decifrado

    alphabet = get_alphabet()   # alfabeto
    length = len(alphabet)      # longitud del alfabeto
    index = 0

    for letter in message:

        try:
            index = alphabet.index(letter)  # indice dentro del alfabeto
        except:
            print "No existe %s en el alfabeto" % (letter,)
            continue

        move = index - key      # nueva posicion
        move = get_index(move,length)

        # debug
        if debug:
            print "move %d"%(move,)


        decrypted += alphabet[move] # agrega al mensaje decifrado

        #debug
        if debug:
            print "%s = %s" % (alphabet[index],alphabet[move])

    return decrypted


# inicio
print "Cifrado por sustitucion"
print "Mensaje:"
message = raw_input()

print "Llave:"
key = int(raw_input())

# mensaje cifrado
crypted = crypt(message,key)
print "Cifrado:" + crypted

print " "
def Cifrar_Cesar(String,Key):
    tmp = ''
    for i in String:
        tmp += chr(ord(i)-Key)
    return tmp

Clave=0;

for Clave in range(9):
    print "Clave: "
    print  Clave
    print "Palabra cifrada: " + Cifrar_Cesar(crypted,Clave)
