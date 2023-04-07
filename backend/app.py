from flask import Flask, render_template, request, jsonify

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
    app.run(debug=True)
