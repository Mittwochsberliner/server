from flask import Flask, request, jsonify

app = Flask(__name__)
available_players = []

@app.route("/register", methods=["POST"])
def register():
    """A player registers as available."""
    data = request.json
    player_ip = data.get("ip")
    if player_ip and player_ip not in available_players:
        available_players.append(player_ip)
    return jsonify({"status": "registered", "players": available_players})

@app.route("/find_match", methods=["GET"])
def find_match():
    """Find an available opponent."""
    if available_players:
        return jsonify({"match": available_players.pop(0)})
    return jsonify({"match": None})

@app.route("/clear", methods=["POST"])
def clear():
    """Clear all available players (for debugging)."""
    global available_players
    available_players = []
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
