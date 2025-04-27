from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplacer ici par ta clé API Perplexity et ton secret token personnel
PERPLEXITY_API_KEY = "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"
SECRET_TOKEN = "Guizmo"

@app.route('/search', methods=['GET'])
def search():
    # Vérifie que le bon token est fourni
    token = request.args.get('secret_token')
    if token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized access. Invalid token."}), 401

    # Récupère les paramètres
    mot_cle = request.args.get('mot_cle')
    nombre_de_resultats = request.args.get('nombre_de_resultats', 5)

    # Appel à Perplexity API
    url = f"https://api.perplexity.ai/search?q={mot_cle}&lang=fr&num_results={nombre_de_resultats}"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": f"Erreur API Perplexity : {response.status_code} - {response.text}"}), response.status_code

# Lancer le serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
