def Cifrar_Cesar(String,Key):
    tmp = ''
    for i in String:
        tmp += chr(ord(i)-Key)
    return tmp

Palabra = raw_input("Introduce la frase: ")

Clave=0;

for Clave in range(9):
    print "Clave: " 
    print  Clave
    print "Palabra cifrada: " + Cifrar_Cesar(Palabra,Clave)
