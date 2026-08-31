#Funciones varias (Ej: barra de carga)

import time

def carga():
    duracion = 5
    pasos = 50
    intervalo = duracion / pasos
    
    for i in range(pasos + 1):
        porcentaje = (i / pasos) * 100
        barra = "█" * i + "░" * (pasos - i)
        print(f"\r[{barra}] {porcentaje:.1f}%", end="", flush=True)
        time.sleep(intervalo)
    
    print("\n¡Completado!")