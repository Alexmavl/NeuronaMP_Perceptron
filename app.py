from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Lógica del Perceptrón (Tarjeta Platinum) ---
def calcular_perceptron(edad, ahorros):
    bias = 0.15
    w1 = 0.01
    w2 = 0.0005
    suma_ponderada = (edad * w1) + (ahorros * w2) + bias
    resultado = 1 if suma_ponderada > 0 else 0
    return {
        "suma": round(suma_ponderada, 4),
        "resultado": resultado,
        "mensaje": "APROBADO" if resultado == 1 else "DENEGADO"
    }

# --- Lógica de la Neurona M-P (Cine) ---
def calcular_neurona_mp(x1, x2, x3, x4):
    theta = 2
    pesos = [1, 1, 1, 1]
    entradas = [x1, x2, x3, x4]
    z = sum(e * p for e, p in zip(entradas, pesos))
    resultado = 1 if z >= theta else 0
    return {
        "z": z,
        "theta": theta,
        "resultado": resultado,
        "mensaje": "SÍ voy al cine" if resultado == 1 else "NO voy al cine"
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
