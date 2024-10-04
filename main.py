from pynput.keyboard import Key, Listener

# Crear dos funciones para cada movimiento del teclado

# Cuando el usuario presiona una tecla
def presionado(tecla):
    print(f"Se presiono la tecla {tecla}")
# Cuando el usuario libera una tecla
def liberado(tecla):
    pass
    #print(f"Se libero la tecla {tecla}")


# Crear un metodo que se encargue de escuchar lo que el teclado recibe
with Listener(on_press = presionado, on_release = liberado) as listener:

    # 1. Se ejecuta de manera continua el metodo Listener
    # 2. Si el usuario presiona una tecla, resultado lo guarda como "listenner"
    # 3. Lo agrega a los resultados

    listener.join()