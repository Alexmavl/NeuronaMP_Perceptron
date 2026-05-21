import sys

def perceptron_tarjeta():
    """
    Tarea 1: Algoritmo Perceptrón (Aprobación Tarjeta Platinum)
    Objetivo: Decidir si se aprueba una tarjeta basado en Edad y Ahorros.
    """
    print("\n--- Simulador de Perceptrón: Aprobación Tarjeta Platinum ---")
    
    # 1. Solicitar las entradas X1 y X2 al usuario
    try:
        x1 = float(input("Ingrese su Edad (X1): "))
        x2 = float(input("Ingrese sus Ahorros en cuenta bancaria (X2): "))
    except ValueError:
        print("Error: Por favor ingrese valores numéricos.")
        return

    # 2. Definir parámetros de la red
    # Bias (b) fijo por requerimiento
    bias = 0.15
    
    # Pesos propuestos lógicamente:
    # W1 (Edad): 0.01 - La edad suma puntos pero de forma moderada.
    # W2 (Ahorros): 0.0005 - Los ahorros son clave. (Ej. 10,000 ahorrados suman 5 puntos).
    # Nota: Dado que bias y pesos son positivos, para obtener un resultado negativo 
    # se requiere que alguna entrada sea negativa (ej. deudas) o valores muy bajos 
    # si los pesos fueran distintos. Para esta simulación, usaremos estos valores.
    w1 = 0.01
    w2 = 0.0005

    # 3. Calcular la suma ponderada (a)
    # Fórmula: a = (X1 * W1) + (X2 * W2) + b
    suma_ponderada = (x1 * w1) + (x2 * w2) + bias
    
    print(f"\nCálculo Interno:")
    print(f"Suma Ponderada = ({x1} * {w1}) + ({x2} * {w2}) + {bias} = {suma_ponderada:.4f}")

    # 4. Aplicar la función de activación (Escalón)
    # Requerimiento: Si a > 0 => 1 (Aprobado), Si a <= 0 => 0 (Denegado)
    if suma_ponderada > 0:
        resultado = 1
        mensaje = "APROBADO (Tarjeta Platinum Concedida)"
    else:
        resultado = 0
        mensaje = "DENEGADO (No cumple los requisitos mínimos)"

    # 5. Imprimir el resultado final
    print(f"\nResultado de la Neurona: {resultado}")
    print(f"Estado Final: {mensaje}")

def neurona_mp_cine():
    """
    Tarea 2: Algoritmo Neurona Artificial M-P (Ir al cine)
    Objetivo: Decidir si ir al cine basado en 4 condiciones booleanas.
    """
    print("\n--- Simulador de Neurona McCulloch-Pitts: ¿Voy al cine? ---")
    
    # 1. Solicitar las 4 entradas booleanas (1 o 0)
    try:
        print("Responda con 1 (Sí) o 0 (No):")
        x1 = int(input("¿Es fin de semana? (X1): "))
        x2 = int(input("¿No tiene tareas pendientes? (X2): "))
        x3 = int(input("¿Está el cine abierto? (X3): "))
        x4 = int(input("¿Se estrena película? (X4): "))
        
        # Validar que sean 0 o 1
        entradas = [x1, x2, x3, x4]
        if any(x not in [0, 1] for x in entradas):
            print("Error: Por favor use solo 0 o 1 para las entradas.")
            return
    except ValueError:
        print("Error: Entrada inválida. Use números (0 o 1).")
        return

    # 2. Parámetros de la Red
    # Umbral (theta) = 2 (Requerimiento)
    theta = 2
    # Pesos excitatorios = 1 (Requerimiento)
    pesos = [1, 1, 1, 1]

    # 3. Calcular la suma de las entradas activas (Z)
    z = sum(x * w for x, w in zip(entradas, pesos))
    
    print(f"\nCálculo Matemático:")
    print(f"Z(X) = {x1} + {x2} + {x3} + {x4} = {z}")
    print(f"Umbral (θ) = {theta}")

    # 4. Evaluar contra el umbral usando estructuras de control
    # Función de activación: a(Z(X)) = 1 si Z(X) >= theta, else 0
    if z >= theta:
        activacion = 1
        decision = "SÍ voy al cine."
    else:
        activacion = 0
        decision = "NO voy al cine."

    # 5. Imprimir la decisión final
    print(f"\nResultado de Activación: {activacion}")
    print(f"Decisión Final: {decision}")

def menu():
    while True:
        print("\n==========================================")
        print("   MENÚ DE REDES NEURONALES - TAREA 8")
        print("==========================================")
        print("1. Perceptrón (Tarjeta Platinum)")
        print("2. Neurona McCulloch-Pitts (Ir al cine)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            perceptron_tarjeta()
        elif opcion == '2':
            neurona_mp_cine()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
