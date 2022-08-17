def suma(num1: int,num2: int) ->int:
    resultado = num1 + num2
    return resultado

resp = suma('Santiago',' Echeverri')
print(resp)



def multiplicacion(num1,num2):
    resultado = num1*num2
    return resultado 

resp = multiplicacion(8,10)
print(resp)


def division(num1,num2):
    try:
        resultado = num1/num2
        return resultado 
    except ZeroDivisionError as e:
        raise 'se está dividiendo por 0, por favor cambie el argumento'
resp = division(10,0)
print(resp)