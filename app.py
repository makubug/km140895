from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Witaj, {name}!"})

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except TypeError:
        return jsonify({"error": "Brak wymaganych parametrów num1 i num2"}), 400

    prediction = 1 if num1 + num2 > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
