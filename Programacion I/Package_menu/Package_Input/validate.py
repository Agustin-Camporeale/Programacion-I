def validate_number(numero:int, minimo:int, maximo:int):
     """ Funcion para validar un numero en determinado rango.Una vez validado el numero devuelve Verdadero o Falso segun corresponda """
     if numero >= minimo and numero <= maximo:
          retorno = True
     else:
          retorno = False
     return retorno

def validate_length(cadena:str,longitud:int):
     """La funcion recibe la longitud de la cadena a validar y lo compara con el maximo.Devuelve Verdadero o Falso segun corresponda """
     retorno = False
     if longitud <= maximo:
          retorno = True
     return retorno
