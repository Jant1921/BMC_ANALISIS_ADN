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
def obtenerLargoHilera(hilera):
	return len(hilera)

"""
obtiene el i-esimo elemento de una hilera
@param {string}   hilera - hilera a utilizar
@param {int} posicion - posicion en la hilera del elemento a obtener
@return {char} i-esimo elemento de la hilera
"""
def obtenerElementoHilera(hilera, posicion):
	return hilera[posicion-1]

"""
determina si un string es sub secuencia de una secuencia
@param {string} secuencia - secuencia a utilizar
@param {string} subSecuencia - sub secuencia que se quiere evaluar
@return {bool} resultado de la comparacion
"""
def esSubSecuencia(secuencia,subSecuencia):
	i = 0
	j = 0
	largoSecuencia = obtenerLargoHilera(secuencia)
	largoSubSecuencia = obtenerLargoHilera(subSecuencia)
	while i < largoSecuencia and j < largoSubSecuencia:
		if secuencia[i] == subSecuencia[j]:
			j = j + 1
		i = i + 1
	return j==largoSubSecuencia

"""
determina si un string es super secuencia de una secuencia
@param {string} secuencia - secuencia a utilizar
@param {string} superSecuencia - super secuencia que se quiere evaluar
@return {bool} resultado de la comparacion
"""
def esSuperSecuencia(secuencia,superSecuencia):
	i = 0
	j = 0
	largoSecuencia = obtenerLargoHilera(secuencia)
	largoSuperSecuenica = obtenerLargoHilera(superSecuencia)
	while i < largoSecuencia and j < largoSuperSecuenica:
		if secuencia[i] == superSecuencia[j]:
			i = i + 1
		j = j + 1
	return i==largoSecuencia

"""
determina si un string es sub string de otra
@param {string} string - secuencia a utilizar
@param {string} subString - sub string que se quiere evaluar
@return {bool} resultado de la comparacion
"""
def esSubString(string,subString):
	return subString in string

"""
determina si un string es super string de otra
@param {string} string - secuencia a utilizar
@param {string} superString - super string que se quiere evaluar
@return {bool} resultado de la comparacion
"""
def esSuperString(string, superString):
	return string in superString



