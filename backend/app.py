from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

flask_app = os.environ.get('FLASK_APP')
flask_env = os.environ.get('FLASK_ENV')
flask_run_host = os.environ.get('FLASK_RUN_HOST')
flask_run_port = os.environ.get('FLASK_RUN_PORT')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add other Flask routes and logic as needed
@app.route('/greet', methods=['POST'])
def greet():
    # Retrieve the name from the request
    name = request.form.get('name')

    # Generate a greeting message
    greeting = f'Hello, {name}! This is a greeting from the server.'

    # Return the greeting as a JSON response
    return jsonify({'greeting': greeting})

if __name__ == '__main__':
    app.env = flask_env

    # Set Flask app run host and port
    app.run(host=flask_run_host, port=int(flask_run_port), debug=True)
