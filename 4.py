import zlib as zl
 
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

def comprimir(line):
	return zl.compress(line)

def descomprimir(line):
	return zl.decompress(line)






line = "jamones"
x=comprimir(cifrar(line))
print (descifrar(descomprimir(x)))
