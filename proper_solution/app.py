from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Comprehensive regex for email validation
EMAIL_REGEX = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+"
    r'(\.[-!#$%&\'*+/=?^_`{}|~0-9A-Z]+)*'
    r'|^"([^\\"]|(\\[\\"]))+"'
    r')@([A-Z0-9-]+\.)+[A-Z]{2,}$', re.IGNORECASE)

@app.route('/validate', methods=['POST'])
def validate_email():
    data = request.get_json()
    email = data.get('email', '')
    if EMAIL_REGEX.match(email):
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 200

@app.route('/healthz', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
