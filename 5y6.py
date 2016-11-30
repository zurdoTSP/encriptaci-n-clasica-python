import zlib as zl
import sys
def cifrar(palabra):
    c="abcdefghijklmnopqrstuvwxyz"
    operacion=0
    cifrado=""
    for i in palabra:
        if i==' ':
            cifrado=cifrado+' '
        else:
            operacion=c.find(i)+3
            operacion=int(operacion)%26
            cifrado=cifrado+c[operacion]
    return cifrado

def descifrar(palabra):
    c="abcdefghijklmnopqrstuvwxyz"
    operacion=0
    cifrado=""
    for i in palabra:
        if i==' ':
            cifrado=cifrado+' '
        else:
            operacion=c.find(i)-3
            operacion=int(operacion)%26
            cifrado=cifrado+c[operacion]
    return cifrado

def comprimir(line):
    return zl.compress(line)

def descomprimir(line):
    return zl.decompress(line)






infile = open('texto.txt', 'r')
x=cifrar(infile.read())

infile.close()
outfile = open('comprimido.txt', 'wb') # Indicamos el valor 'w'.
outfile.write(comprimir(x.encode()))
outfile.close()

infile = open('comprimido.txt', 'rb')

x=infile.read()
x=descomprimir(x)
print(descifrar(str(x)))
infile.close()
#print (descifrar(descomprimir(x)))
