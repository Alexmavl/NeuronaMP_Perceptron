# Guion Técnico: Demostración de Redes Neuronales (Web App - Tarea 8)

**Estudiante:** Marvin Alexander Vásquez López  
**Carnet:** 1790-22-12802  
**Duración Estimada:** 3 - 5 Minutos  

---

## Estructura del Video

### 1. Introducción y Presentación (0:00 - 1:00)
*   **Qué mostrar:** La aplicación web abierta en el navegador. Resalta el encabezado con el logo de la UMG y tus datos.
*   **Narración:** "Buen día, Ing. Carmelo Mayen. Mi nombre es Marvin Alexander Vásquez López y hoy presentaré mi proyecto de Redes Neuronales Básicas para el curso de Inteligencia Artificial. Como pueden observar, he desarrollado una aplicación web profesional con una interfaz moderna en tonos azul marino para modelar el Perceptrón y la Neurona McCulloch-Pitts."

### 2. Tarea 1: Perceptrón (Tarjeta Platinum) (1:00 - 2:15)
*   **Qué mostrar:** La sección izquierda de la web.
*   **Narración:** 
    *   "El primer modelo es un Perceptrón para la aprobación de tarjetas de crédito. Aquí ingresamos la Edad y los Ahorros."
    *   "La lógica utiliza una suma ponderada con un Bias de 0.15. He asignado pesos que priorizan la solvencia económica."
*   **Prueba en vivo:** 
    *   Ingresa Edad=28, Ahorros=15000. Haz clic en 'Analizar'. Muestra el resultado verde (APROBADO).
    *   Ingresa Edad=20, Ahorros=-2000. Haz clic en 'Analizar'. Muestra el resultado rojo (DENEGADO).

### 3. Tarea 2: Neurona McCulloch-Pitts (Ir al cine) (2:15 - 3:30)
*   **Qué mostrar:** La sección derecha de la web.
*   **Narración:**
    *   "El segundo modelo es la Neurona M-P para decidir si ir al cine. Esta neurona utiliza un umbral o theta de 2."
    *   "A diferencia del perceptrón, aquí las entradas son binarias, representadas por estos interruptores."
*   **Prueba en vivo:**
    *   Activa '¿Es fin de semana?' y '¿Cine abierto?'. Haz clic en 'Evaluar'. Muestra el resultado (SÍ voy).
    *   Deja solo uno activo. Muestra el resultado (NO voy).

### 4. Conclusión y Código (3:30 - 4:00)
*   **Qué mostrar:** VS Code brevemente (app.py) y luego regresa a la web.
*   **Narración:** "La aplicación fue construida con Python y Flask en el backend, y un diseño personalizado en el frontend. Esto permite una experiencia mucho más profesional y clara para el usuario final. Muchas gracias."
