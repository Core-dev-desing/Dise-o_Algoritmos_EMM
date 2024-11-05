def revertir_vocales(S):
   
    A = list(S)
    
   
    diccionario_vocales = {
        'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
        'A': True, 'E': True, 'I': True, 'O': True, 'U': True
    }
    
   
    i = 0
    j = len(A) - 1
    
   
    while i < j:
      
        if A[i] not in diccionario_vocales:
            i += 1
       
        elif A[j] not in diccionario_vocales:
            j -= 1
       
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    
   
    return ''.join(A)

# Ejemplo de uso
cadena = "lapiz"
resultado = revertir_vocales(cadena)
print(resultado)  # Debería imprimir "lipaz"
            


