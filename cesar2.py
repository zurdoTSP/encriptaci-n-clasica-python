import sys
def cifrar(palabra):
    c="abcdefghijklmnopqrstuvwxyz"
    operacion=0
    cifrado=""
    for i in palabra:
        operacion=c.find(i)+3
        operacion=int(operacion)%26
        cifrado=cifrado+c[operacion]
    return cifrado

def descifrar(palabra):
    c="abcdefghijklmnopqrstuvwxyz"
    operacion=0
    cifrado=""
    for i in palabra:
        operacion=c.find(i)-3
        operacion=int(operacion)%26
        cifrado=cifrado+c[operacion]
    return cifrado


print(descifrar(cifrar("hola")))
