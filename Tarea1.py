import sys
import random
BASES_ADN = ['A','C','T','G','a','c','t','g']
BASES_ARN = ['A','C','U','G','a','c','u','g'] 
SECUENCIA_PRUEBA_ADN = 'attggttatgaaaggactctacgctc'

basesARN= {"A":"Adenina",
        "C":"Citosina",
        "U":"Uracilo",
        "G":"Guanina"}

basesADN= {"A":"Adenina",
        "C":"Citosina",
        "T":"Timina",
        "G":"Guanina"}
"""
Genera una cadena de ADN de N caracteres
@param {int} longitud - Cantidad de caracteres de la secuencia de ADN
@return {string} cadena de ADN
"""
def ADNaleatorio(longitud):
        chain=''
        for i in range(longitud):
                chain+=BASES_ADN[random.randint(0,3)]
        return chain
        

"""
valida si un caracter dado es valido dentro de una lista de bases (ADN/ARN)
@param {string} chain - cadena de caracteres
@param {int} position - posicion de la lista a consultar
@return {string} nombre de la base
"""
def obtenerBaseADN(chain,position):
        length = chain.__len__()
        if (length + 1 <= position):
                print ("Posicion invalida\nIngrese un valor valido")
                return False
        base=basesADN[chain[position-1]]
        print ("Base nitrogenada: " + base)
        return base
"""
valida si un caracter dado es valido dentro de una lista de bases (ADN/ARN)
@param {string} chain - cadena de caracteres
@param {int} position - posicion de la lista a consultar
@return {string} nombre de la base
"""
def obtenerBaseARN(chain,position):
        length = len(chain)
        if (length + 1 <= position):
                print ("Posicion invalida\nIngrese un valor valido")
                return False
        base=basesARN[chain[position-1]]
        print ("Base nitrogenada: " + base)
        return base

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
        if posicion==0 or len(hilera)<abs(posicion):
                return "La posicion no es valida"
        elif posicion<0:
                return hilera[posicion]
        else:
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

"""
Concatena dos hileras
@param {string} string - hilera de inicio
@param {string} string2 - hilera que se adjuntara al final
@return {string} hilera que contiene a las hileras string y string2
"""
def concatenarHileras(string,string2):
        return string+string2

""" 
Calcula el complemento de cada base nitrogenada de una cadena
@param {string} hilera - hilera de bases nitrogenadas
@return {string} hilera con el complemento de las bases nitrogenadas de la hilera introducida
"""
def calcularComplementoADN(hilera):
        pos=0
        hilera=hilera.upper()
        largo=len(hilera)
        complemento=''
        while pos < largo:
                if hilera[pos] == 'A':
                        complemento+='T'
                elif hilera[pos]=='T':
                        complemento+='A'
                elif hilera[pos]=='C':
                        complemento+='G'
                elif hilera[pos]=='G':
                        complemento+='C'
                pos+=1
        return complemento

"""
Calcula el complemento de cada base nitrogenada de una cadena
@param {string} hilera - hilera de bases nitrogenadas
@return {string} hilera con el complemento de las bases nitrogenadas de la hilera introducida
"""
def calcularComplementoInversoADN(hilera):
        hilera=hilera[::-1]
        pos=0
        hilera=hilera.upper()
        largo=len(hilera)
        complemento=''
        while pos < largo:
                if hilera[pos] == 'A':
                        complemento+='T'
                elif hilera[pos]=='T':
                        complemento+='A'
                elif hilera[pos]=='C':
                        complemento+='G'
                elif hilera[pos]=='G':
                        complemento+='C'
                pos+=1
        return complemento
"""
Verifica si una hilera es palindroma
@param {string} hilera - hilera a evaluar
@return {bool} resultado de la evaluacion
"""
def verificarPalindromo(hilera):
        palindromo=hilera[::-1]
        return hilera==palindromo
"""
Transforma una hilera de bases de ADN a ARN
@param {string} hilera - hilera de bases de ADN
@return {string} hilera transformada
"""
def ADNtoARN(hilera):
        hilera=hilera.replace('T','U')
        return hilera
"""
Transforma una hilera de bases de ARN a ADN
@param {string} hilera - hilera de bases de ARN
@return {string} hilera transformada
"""
def ARNtoADN(hilera):
        hilera=hilera.replace('U','T')
        return hilera

"""
Carga una hilera desde un archivo
@param {string} hilera - hilera donde almacenar los datos
@param {string} direccion - hilera que corresponde a la direccion del archivo
@return {string} hilera leida del archivo o ultima hilera valida
"""
def cargarHilera(hilera,direccion):
        try:
                temporal=''
                if (hilera!=''):
                        temporal=hilera
                archivo=open(direccion)
                hilera=archivo.read()
                archivo.close()
                if(hilera=='' and temporal == ''):
                        print('Archivo vacio invalido \ningrese el nombre del archivo que desea leer')
                elif(hilera=='' and temporal != ''):
                        print('Archivo vacio invalido \nSe continua trabajando con la ultima hilera valida introducida')
                        hilera=temporal
                return hilera
        except IOError as error:
                print "I/O error, la ruta especificada no es valida. Error({0}): {1}".format(error.errno,error.strerror)
                if(hilera!=''):
                        print("Se continua trabajando con el ultimo archivo valido")
                return hilera
"""
Carga una hilera desde un archivo
@param {string} hilera - Cadena a guardar
@param {string} direccion - hilera que corresponde a la direccion del archivo
@return {bool} Confirma el exito de la operacion 
"""       
def crearArchivo(hilera,direccion):
        try:
                archivo=open(direccion,'w')
                archivo.write(hilera)
                archivo.close()
        except:
                print("Error inesperado: ",sys.exc_info()[0])
        

########################################                Main            ##############################################
print("Bienvenido\nIngrese el nombre del archivo que desea leer,\n si desea generar una secuencia aleatoria ingrese 'aleatoria'")
salir=False
hilera=''
hilera2=''
longitud=0
while (hilera==''):
        direccion=input()
        if(direccion=='aleatoria'):
                while(longitud==0):
                        print('Ingrese el largo de la secuencia deseada')
                        longitud=int(input())
                        if(longitud<0):
                                longitud=0;
                        hilera=ADNaleatorio(longitud)
        else:
                hilera=cargarHilera(hilera,direccion)
                
print("Ingrese el numero que corresponda a la funcion deseada")
while(salir==False):
        print("15.Salir \n1.Cambiar Archivo \n2.Cargar en una segunda hilera \n3.Ver mis hileras actuales \n4.Guardar Hilera en txt \n5.Generar cadena de ADN aleatoria \n6.Verificar si la hilera es palindromo")
        opcion=input()
        if (opcion==15):
                salir=True
                sys.exit()
                
        elif(opcion==1):
                print("Ingrese el nombre del archivo que desea leer")
                direccion=input()
                hilera=cargarHilera(hilera,direccion)
        elif(opcion==2):
                print("Ingrese el nombre del archivo que desea leer")
                direccion=input()
                hilera2=cargarHilera(hilera2,direccion)
        elif(opcion==3):
                print("Hilera: "+ hilera)
                print("\nHilera2: "+ hilera2)
        elif(opcion==4):
                print("Ingrese el nombre del archivo que desea crear (Tenga en cuenta que si el archivo ya existe, sera eliminado)")
                direccion=input()
                crearArchivo(hilera,direccion)
        elif(opcion==5):
                longitud=0
                while(longitud==0):
                        print('Ingrese el largo de la secuencia deseada')
                        longitud=int(input())
                        if(longitud<0):
                                longitud=0;
                        hilera=ADNaleatorio(longitud)
                
                
        
                        
        
        


        

