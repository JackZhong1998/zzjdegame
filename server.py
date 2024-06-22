from flask import Flask, request, jsonify # type: ignore
import api_handler
import game_logic
import database
import user_management

app = Flask(__name__)

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    data = request.get_json()
    description = data['description']
    code = api_handler.generate_code(description)
    return jsonify({'code': code})

@app.route('/api/save-game', methods=['POST'])
def save_game():
    data = request.get_json()
    game_state = data['game_state']
    database.save_game_state(game_state)
    return jsonify({'status': 'success'})

@app.route('/api/load-game', methods=['GET'])
def load_game():
    game_state = database.load_game_state()
    return jsonify({'game_state': game_state})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user_management.register_user(username, password)
    return jsonify({'status': 'success'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if user_management.login_user(username, password):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

if __name__ == '__main__':
    app.run(debug=True)