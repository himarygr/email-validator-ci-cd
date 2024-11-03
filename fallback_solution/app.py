from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate_email():
    data = request.get_json()
    email = data.get('email', '')
    if '@' in email:
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 200

@app.route('/healthz', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
