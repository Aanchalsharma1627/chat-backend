from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')
    user_name = data.get('user', 'User')
    response = f"Hello {user_name}, you said: '{user_msg}'"
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run()
