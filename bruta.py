def cifrar(palabra):
	c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	operacion=0
	cifrado=""
	for i in palabra:
		operacion=c.find(i)+100
		operacion=int(operacion)%52
		cifrado=cifrado+c[operacion]
	return cifrado

def descifrar(palabra):
	c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	operacion=0
	contador=1
	descifrado=""
	x=False
	while(x==False):
		descifrado=""
		for i in palabra:
			operacion=c.find(i)-contador
			operacion=int(operacion)%52
			descifrado=descifrado+c[operacion]
		print descifrado
		contador=contador+1
		if(descifrado=="holasMisusMeLlamoAntonio"):
			x=True
		
print(cifrar("holasMisusMeLlamoAntonio"))
descifrar(cifrar("holasMisusMeLlamoAntonio"))
