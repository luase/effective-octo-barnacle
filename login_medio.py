"""
    Vamos a ejemplificar un login en 3 niveles de dificultad,
    el presente codigo es para el nivel intermedio, a diferencia
    del anterior vamos a incluir una cantida de intentos maxima y
    la forma de proteger el codigo de las personas que no tengan
    acceso

    El resto de ejemplos los encuentras en:
        https://github.com/luase/effective-octo-barnacle
"""

if __name__ == "__main__":
    # Definamos nuestro usuario y nuestra contraseña aquí.
    # Estas son secreto del programa, las personas que no
    # hayan leído el código no deberían saberlas.
    USUARIO = 'jimmy'
    CONTRASENA = 'ymmij'

    #  Definamos aqui la cantidad de intentos permitidos
    INTENTOS = 3

    # Vamos a controlar la cantidad de repeticiones
    # dentro del ciclo usando nuestra variable 'intentos',
    # nuestras condiciones de escape son 2:
    #  * que se termine la cantidad de intentos posibles
    #  * que acceda correctamente
    #
    # Usar un ciclo while, con la condicion True
    # como se ejemplifica debajo, puede causar un bucle
    # infinito si no tiene una instruccion de salida.
    # En este ejemplo vamos a usar break y exit().
    while True:
        # Antes de dejarle intentar, veamos si tiene intentos
        if INTENTOS == 0:
            # En caso de que no tenga intentos, terminaremos
            # con el programa
            exit()
        username = input('Ingrese su nombre de usuario:\n > ')
        password = input('Ingrese la contraseña:\n > ')
        # revisemos si son correctos
        if username == USUARIO:
        # En este punto, la persona ingreso correctamente
        # el usuario, comprobemos la contraseña ahora.
            if password == CONTRASENA:
                # Llegado a este punto, el ciclo puede terminar
                # la persona ingreso correctamente usuario y
                # contrasena
                break
        else:
            # En caso de que el usuario no sea correcto,
            # no hace falta ya comprobar la contrasena.
            # Le restamos un intento directamente.
            INTENTOS = INTENTOS - 1
