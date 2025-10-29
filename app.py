from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json(force=True)
    message = data.get('message', '')
    return jsonify({
        'received': message,
        'response': f'You sent: {message}'
    })

if __name__ == '__main__':
    app.run(debug=True)