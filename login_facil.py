"""
    Vamos a ejemplificar un login en 3 niveles de dificultad,
    este es el login en escencia.

    Un 'Login' es en escencia comprobar si una combinación
    de usuario y contraseña son correctos
"""

# Este primer if lo van a encontrar seguido en programas escritos
# en el lenguaje de Python, es smilar al 'main' en otros lenguajes.
# Revisa: https://alvarohurtado.es/2020/11/16/que-hace-if-__name__-__main__-en-python/
if __name__ == "__main__":
    # Definamos nuestro usuario y nuestra contraseña aquí.
    # Estas son secreto del programa, las personas que no
    # hayan leído el código no deberían saberlas.
    USUARIO = 'jimmy'
    CONTRASENA = 'ymmij'

    # Ahora le toca a la persona interactuando con el programa
    # ingresar un par de usuario-contraseña. Experimenta modificando
    # el texto entre las '' para personalizar la experiencia de usuario
    username = input('Ingrese su nombre de usuario:\n > ')
    password = input('Ingrese la contraseña:\n > ')

    # El último paso para crear un login es comprobar si
    # los datos que ingresaron son válidos o incorrectos.

    # Primero comprobemos los usuarios, podemos comparar
    # directamente el par usuario-contraseña, pero esto nos
    # dará la flexibilidad de hacer cosas interesantes,
    # como decir un mensaje acerca del error que la persona
    # cometió
    if username == USUARIO:
        # En este punto, la persona ingreso correctamente
        # el usuario, comprobemos la contraseña ahora.
        if password == CONTRASENA:
            # La persona que interactua con el programa
            # únicamente verá este mensaje si el par
            # de usuario-contraseña que introdujo son correctos.
            print("Buen día! Bienvenido al programa, Jimmy")
        else:
            print("Contraseña erronea")
    else:
        print('El usuario no existe')
