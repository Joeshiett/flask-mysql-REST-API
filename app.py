from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({'message': 'Welcome to Flask!'})

@app.get('/hello')
def hello():
    return jsonify({'message': 'Hello World'})


if __name__ == '__main__':
    app.run(debug=True)