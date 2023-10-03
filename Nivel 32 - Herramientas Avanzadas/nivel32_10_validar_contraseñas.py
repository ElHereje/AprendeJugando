'''
RETO --> define una función que valide contraseñas. (VISTO EN NIVEL 11 MAS SIMPLE)
Ha de comprobar:
- Entre 6 y 12 caracteres
- Al menos un dígito
- Al menos una letra
- Al menos una mayusc.
- Al menos una minusc.
- Al menos un carcater especial

Se debe avisar de la 1ª que ocurra, en ese orden

mas o menos sería:    
# entre 6 y 12 caracteres
    if 5 < len(contraseña) < 13:
        # algún dígito
        if any([caracter.isdigit() for carater in contraseña]):
            # alguna letra minuscula
            if any([caracter.islower() for carater in contraseña]):
                # alguna letra mayuscula
                if any([caracter.isupper() for carater in contraseña]):
                    # algún caracter
                    if any([True if caracter in string.punctuation else False for caracter in contraseña]):
                        print("Contraseña establecida de manera correcta...")
                        return True
                    else:
                        print("La contraseña debe tener algún caracter especial...")
                else:
                    print("La contraseña debe tener alguna mayúscula")
            else:
                print("La contraseña debe tener alguna minúscula...")
        else:
            print("La contraseña debe tener algún dígito...")
    else:
        print("La contraseña debe tener entre 6 y 12 caracteres...")
    return False


'''

# una manera más simple es verificar lo contrario y concatenar con elif

from string import punctuation # para los carcateres

def valida_contraseña(contraseña):

    if len(contraseña) < 6 or len(contraseña) > 12:
        print("La contraseña debe tener entre 6 y 12 caracteres...")
    elif not any([caracter.isdigit() for caracter in contraseña]):
        print("La contraseña debe tener algún dígito...")
    elif not any([caracter.islower() for caracter in contraseña]):
        print("La contraseña debe tener alguna minúscula...")
    elif not any([caracter.isupper() for caracter in contraseña]):
        print("La contraseña debe tener alguna mayúscula")
    elif not any([True if caracter in punctuation else False for caracter in contraseña]):
        print("La contraseña debe tener algún caracter especial...")
    else:
        print("Contraseña establecida de manera correcta...")
        return True
    return False

intentos = 0
while True:
    contra = input("Introduce Contraseña: ")
    intentos += 1

    if valida_contraseña(contra):
        print(f"La contraseña introducida ha sido {contra}")
        break
    elif intentos > 5:
        contra = None
        print("No ha sido posible establecer la contraseña...")
        break
