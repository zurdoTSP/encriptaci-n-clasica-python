import sys
import zlib as zl
def comprimir(line):
	return zl.compress(line)

#caesarenc texto.txt -o salida.enc

infile = open(sys.argv[2], 'r')

print('>>> Lectura completa del fichero')
for x in infile:
	print x
	x=x.replace('\n','')
	infil2 = open(x, 'r')
	z=comprimir(infil2.read())
	y=str(infil2)
	print("la original es ",len(y), "la comprimida es: ",len(z))
	y=""
	infil2.close()
	
#outfile = open(sys.argv[4], 'w') 
#outfile.write(cifrar(infile.read()))

#print("hecho")

infile.close()
#outfile.close()
