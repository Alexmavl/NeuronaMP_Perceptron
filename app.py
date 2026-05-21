from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Lógica del Perceptrón (Tarjeta Platinum) ---
def calcular_perceptron(edad, ahorros):
    bias = 0.15
    w1 = 0.01
    w2 = 0.0005
    suma_ponderada = (edad * w1) + (ahorros * w2) + bias
    resultado = 1 if suma_ponderada > 0 else 0
    
    # Formato según PDF Clase 11
    linea1 = f"Z = (X1*W1 + X2*W2) + b"
    linea2 = f"Z = ({edad} * {w1} + {ahorros} * {w2}) + {bias}"
    linea3 = f"Z = {round(suma_ponderada, 4)}"
    linea4 = f"Evaluación: {round(suma_ponderada, 4)} > 0" if resultado == 1 else f"Evaluación: {round(suma_ponderada, 4)} <= 0"
    
    clase_bg = "bg-aprobado" if resultado == 1 else "bg-denegado"
    texto_res = "APROBADO" if resultado == 1 else "DENEGADO"
    evaluacion = f"<div class='result-highlight {clase_bg}'>Resultado Final: {texto_res}</div>"
    
    procedimiento_alert = f"{linea1}\n{linea2}\n{linea3}\n{linea4}\n\n{evaluacion}"
    
    return {
        "resultado": resultado,
        "mensaje": "APROBADO" if resultado == 1 else "DENEGADO",
        "procedimiento_completo": procedimiento_alert
    }

# --- Lógica de la Neurona M-P (Cine) ---
def calcular_neurona_mp(x1, x2, x3, x4):
    theta = 2
    entradas = [x1, x2, x3, x4]
    z = sum(entradas)
    resultado = 1 if z >= theta else 0
    
    # Formato según PDF Clase 10
    linea1 = f"Z = X1 + X2 + X3 + X4"
    linea2 = f"Z = {x1} + {x2} + {x3} + {x4}"
    linea3 = f"Z = {z}"
    linea4 = f"Evaluación: {z} >= {theta}" if resultado == 1 else f"Evaluación: {z} < {theta}"
    
    clase_bg = "bg-si" if resultado == 1 else "bg-no"
    texto_res = "SÍ VOY AL CINE" if resultado == 1 else "NO VOY AL CINE"
    evaluacion = f"<div class='result-highlight {clase_bg}'>Resultado Final: {texto_res}</div>"
    
    procedimiento_alert = f"{linea1}\n{linea2}\n{linea3}\n{linea4}\n\n{evaluacion}"
    
    return {
        "resultado": resultado,
        "mensaje": "SÍ voy al cine" if resultado == 1 else "NO voy al cine",
        "procedimiento_completo": procedimiento_alert
    }

@app.route('/')
def index():
    return render_template('index.html', 
                           catedra="Inteligencia Artificial",
                           catedratico="Ing. Carmelo Mayen",
                           desarrollador="Marvin Alexander Vásquez López",
                           carnet="1790-22-12802")

@app.route('/api/perceptron', methods=['POST'])
def api_perceptron():
    data = request.json
    try:
        edad = float(data.get('edad', 0))
        ahorros = float(data.get('ahorros', 0))
        return jsonify(calcular_perceptron(edad, ahorros))
    except ValueError:
        return jsonify({"error": "Valores numéricos inválidos"}), 400

@app.route('/api/neurona_mp', methods=['POST'])
def api_neurona_mp():
    data = request.json
    try:
        x1 = int(data.get('x1', 0))
        x2 = int(data.get('x2', 0))
        x3 = int(data.get('x3', 0))
        x4 = int(data.get('x4', 0))
        return jsonify(calcular_neurona_mp(x1, x2, x3, x4))
    except ValueError:
        return jsonify({"error": "Valores booleanos inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)
