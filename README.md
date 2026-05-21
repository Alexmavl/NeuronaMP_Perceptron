# Tarea 8: Neurona M-P y Perceptrón - Inteligencia Artificial

Este proyecto es una aplicación web interactiva desarrollada para la cátedra de **Inteligencia Artificial**. El objetivo es demostrar el funcionamiento práctico de dos modelos fundamentales de redes neuronales: el **Perceptrón** y la **Neurona de McCulloch-Pitts (M-P)**, aplicados a casos de uso de la vida real.

## 🚀 Propósito de la Tarea
La tarea busca ejemplificar cómo las neuronas artificiales toman decisiones binarias basadas en entradas y pesos:
1.  **Perceptrón (Aprobación de Tarjeta Platinum):** Evalúa si un cliente califica para un crédito basado en su edad y ahorros, utilizando una suma ponderada y un sesgo (bias).
2.  **Neurona M-P (Decisión de Ir al Cine):** Una neurona lógica que evalúa condiciones excitatorias (fin de semana, tareas, estreno) frente a un umbral fijo para tomar una decisión.

## 🛠️ Stack Tecnológico
La aplicación está construida con tecnologías modernas y eficientes:
*   **Backend:** Python 3.x con [Flask](https://flask.palletsprojects.com/) (Micro-framework web).
*   **Frontend:** HTML5, CSS3 (Diseño profesional "Clean & Light") y JavaScript (Vanilla JS para llamadas asíncronas a la API).
*   **Servidor:** Flask Development Server.

## 📋 Funcionalidades
*   **Simulación en Tiempo Real:** Realiza cálculos instantáneos sin recargar la página.
*   **Visualización de Fórmulas:** Tarjeta dedicada que explica la matemática detrás de cada modelo.
*   **Interfaz Profesional:** Diseño limpio, responsivo y optimizado para una experiencia de usuario clara.

## ⚙️ Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
Abre una terminal y ejecuta el siguiente comando:
```bash
git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
cd NOMBRE_DEL_REPOSITORIO
```

### 2. Crear un entorno virtual (Opcional pero recomendado)
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias
Asegúrate de tener `pip` instalado y ejecuta:
```bash
pip install flask
```

### 4. Ejecutar la aplicación
Inicia el servidor de Flask:
```bash
python app.py
```
Luego, abre tu navegador y dirígete a: `http://127.0.0.1:5000`

## 📦 Dependencias Necesarias
El proyecto es ligero y solo requiere:
*   `Flask==3.0.0` (o superior)
*   `Python 3.8+`

---
**Desarrollado por:** Marvin Alexander Vásquez López  
**Carnet:** 1790-22-12802  
**Universidad Mariano Gálvez de Guatemala**  
**Noveno Semestre - Inteligencia Artificial**
