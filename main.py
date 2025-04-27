from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplacer par ta clé API Perplexity valide
PERPLEXITY_API_KEY = "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"
SECRET_TOKEN = "Guizmo"

PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

@app.route('/search', methods=['GET'])
def search():
    token = request.args.get('secret_token')
    if token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized access. Invalid token."}), 401

    mot_cle = request.args.get('mot_cle')
    nombre_de_resultats = request.args.get('nombre_de_resultats', 5)

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "pplx-7b-online",  # modèle de Perplexity (modifier si besoin)
        "messages": [
            {"role": "user", "content": f"Donne-moi {nombre_de_resultats} tendances sur : {mot_cle}"}
        ]
    }

    response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": f"Erreur API Perplexity : {response.status_code} - {response.text}"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

