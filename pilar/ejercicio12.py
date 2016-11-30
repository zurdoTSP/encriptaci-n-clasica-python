
import string
def contar(x):
    texto = open("ejer12texto.txt", "r")
    parrafo = texto.read()
    contador=0
    #print parrafo
    for i in parrafo:
        if(x==i):
            contador=contador+1
    return contador

all_chars = list(string.ascii_lowercase)
for i in all_chars:
    x=contar(i)
    print "La letra: " + i + " sale:"
    print x
