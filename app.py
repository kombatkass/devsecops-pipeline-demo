import os
import pickle
from flask import Flask, request

app = Flask(__name__)

# hardcoded secret for TruffleHog to catch
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/ping')
def ping_target():
    target = request.args.get('target')
    # Command Injection sink for Semgrep to catch
    os.system(f"ping -c 1 {target}")
    return "Ping executed."

@app.route('/load_session', methods=['POST'])
def load_session():
    session_data = request.data
    # Insecure Deserialization sink for Semgrep 
    user = pickle.loads(session_data)
    return f"Welcome back, {user['name']}"

if __name__ == '__main__':
    app.run(debug=True)
