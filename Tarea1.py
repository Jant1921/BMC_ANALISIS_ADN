BASES_ADN = ['A','C','T','G','a','c','t','g']
BASES_ARN = ['A','C','U','G','a','c','u','g'] 
SECUENCIA_PRUEBA_ADN = 'attggttatgaaaggactctacgctc'

"""
valida si un caracter dado es valido dentro de una lista de bases (ADN/ARN)
@param {char}   caracter - caracter a validar
@param {char[]} listaBases - lista de caracteres validos para ARN o ADN
@return {bool} resultado de la verificacion
"""
def esBaseValida(caracter, listaBases):
	if(caracter in listaBases):
		return True
	else:
		return False

"""
valida si una secuencia dada es valida dentro de una lista de bases (ADN/ARN)
@param {string}   secuencia - secuencia a validar
@param {char[]} listaBases - lista de caracteres validos para ARN o ADN
@return {bool} resultado de la verificacion
"""
def esSecuenciaValida(secuencia,listaBases):
	for caracter in secuencia:
		if(not esBaseValida(caracter, listaBases)):
			return False
	return True

"""
obtiene el largo de una hilera
@param {string}   hilera - hilera a utilizar
@return {int} largo de la hilera
"""
def largoHilera(hilera):
	return len(hilera)

