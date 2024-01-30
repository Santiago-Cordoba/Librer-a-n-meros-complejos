import math
#Libreria de numeros complejos
#hecho por Santiago Córdoba Dueñas

#suma numeros complejos
def suma(a,b):
    Partereal = a[0]+b[0]
    Parteimaginaria = a[1]+b[1]
    return Partereal,Parteimaginaria

#multiplicacion numeros complejos
def multiplicacion(a,b):
    Partereal = (a[0]*b[0])-(a[1]*b[1])
    Parteimaginaria = (a[0]*b[1])+(b[0]*a[1])
    return Partereal,Parteimaginaria

#resta numeros complejos
def resta(a,b):

    Partereal = a[0]-b[0]
    Parteimaginaria = a[1]-b[1]
    return Partereal,Parteimaginaria

#division numeros complejos
def division(a,b):

    try:
        denominador = b[0] ** 2 + b[1] ** 2
        Partereal = (a[0] * b[0] + a[1] * b[1]) / denominador
        Parteimaginaria = (a[1] * b[0] - a[0] * b[1]) / denominador
        return (Partereal,Parteimaginaria)
    except:
        return ' No se puede realizar la operación de división.'

#modulo numeros complejos
def moduloc(c):

    modulo = (c[0] ** 2 + c[1] ** 2)
    return round(math.sqrt(modulo),2)

#conjugado numeros complejos
def conjugado(c):

    Partereal = c[0]
    Parteimaginaria = c[1] * -1
    return Partereal, Parteimaginaria

#conversion de polar a cartesiano numeros complejos
def polar_a_cartesiano(c):

    Partereal = round(c[0] * math.cos(c[1]),2)
    Parteimaginaria = round(c[0] * math.sin(c[1]),2)
    return Partereal, Parteimaginaria

#fase numeros complejos
def fasec(c):

    if c[0] < 0 and c[1] < 0:
        fase = round(2 * math.pi - (-1 * (math.atan2(c[1], c[0]))), 2)
        return fase
    elif c[0] > 0 > c[1]:
        fase = round((2 * math.pi + math.atan2(c[1], c[0])),2)
        return fase
    else:
        fase = round((math.atan2(c[1], c[0])),2)
        return fase



if __name__ == "__main__":

    c1 = (5.5, -9)
    c2 = (-3, 6)
    c3 = (1, 2)
    c4 = (4, -0.5)

    print("El resultado de la suma es:",suma(c1, c2))
    print("El resultado de la suma es:",suma(c3, c4))
    print("El resultado de la multiplicacion es:",multiplicacion(c1, c2))
    print("El resultado de la multiplicacion es:",multiplicacion(c3, c4))
    print("El resultado de la resta es:",resta(c1, c2))
    print("El resultado de la resta es:",resta(c3, c4))
    print("El resultado de la division es:",division(c1, c2))
    print("El resultado de la division es:",division(c3, c4))
    print("El resultado de la moduloc es:",(moduloc(c1)))
    print("El resultado de la moduloc es:",(moduloc(c2)))
    print("El resultado de la conversion es:",polar_a_cartesiano(c1))
    print("El resultado de la conversion es:",polar_a_cartesiano(c2))
    print("El resultado de la conjugado es:",conjugado(c1))
    print("El resultado de la conjugado es:",conjugado(c2))
    print("El resultado de la fase es:",fasec(c1))
    print("El resultado de la fase es:",fasec(c2))