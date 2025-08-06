from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json()
    print("Payload recebido:", req)

    resposta = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": ["Olá! Sou o Chatbot da Vigilância Sanitária."]
                    }
                }
            ]
        }
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
