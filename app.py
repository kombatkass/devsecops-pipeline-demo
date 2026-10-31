import os
import pickle
from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

# hardcoded secret for TruffleHog to catch
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


@app.route('/ping')
def ping_target():
    target = request.args.get('target')
    #subprocess with a strict list of arguments instead of OS
    subprocess.run(["ping", "-c", "1", target])
    return "Ping executed."

@app.route('/load_session', methods=['POST'])
def load_session():
    session_data = request.data
    #using json instead of pickle for untrusted data
    user = json.loads(session_data)
    return f"Welcome back, {user.get('name', 'User')}"

if __name__ == '__main__':
    #debug mode disabled
    app.run(debug=False)
