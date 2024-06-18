def entero_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

def fraccion_a_binario(fraccion, precision=23):
    binario = "0."
    while fraccion > 0 and len(binario) - 2 < precision:  # len(binario) - 2 para descontar "0."
        fraccion *= 2
        if fraccion >= 1:
            binario += '1'
            fraccion -= 1
        else:
            binario += '0'
    return binario

def calcular_exponente_y_normalizar(binario):
    posicion_coma = 0
    binario = list(binario)
    for indice, posicion in enumerate(binario):
        if(posicion == '.'):
            posicion_coma = indice
            break
    binario.remove('.')
    binario.insert(1, '.')
    binario = ''.join(binario)
    return posicion_coma - 1, binario

def calcular_mantisa(fraccion, precision=23):
    # Remover el "1." de la fracción normalizada
    # Agregar ceros para completar la precisión deseada
    mantisa = fraccion.ljust(precision, '0')
    return mantisa

def main():
    num = input("Ingresar el número con un +/-, sino se tomará como +\n")
    signo = ''
    if(num[0] == '+'):
        signo = True
        num = num[1:]
    elif(num[0] == '-'):
        signo = False
        num = num[1:]
    else:
        signo = True
    num = float(num)
    num_entero = int(num)
    num_decimal = (num - num_entero) #Problema

    binario_entero = entero_a_binario(num_entero)
    binario_fraccion = fraccion_a_binario(num_decimal)
    binario = str(binario_entero)+str(binario_fraccion)[1:]
    print(num_entero, signo, num_entero, num_decimal, binario)

    exponente, nuevo_binario = calcular_exponente_y_normalizar(binario)
    print(exponente, nuevo_binario)

    exponente_sesgado = 127 + exponente
    exponente_sesgado_binario = str(entero_a_binario(exponente_sesgado))
    print(exponente_sesgado, exponente_sesgado_binario)

    binario_fraccion = nuevo_binario[2:]
    mantisa = calcular_mantisa(binario_fraccion)
    print(binario_fraccion, mantisa) 
    bit_signo = ''
    if(signo): bit_signo = '1'
    else: bit_signo = '0'
    return bit_signo +'|'+ exponente_sesgado_binario +'|'+ mantisa

numero_IEEE = main()
print(numero_IEEE)