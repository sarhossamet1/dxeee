from flask import Flask, request, jsonify
app = Flask(__name__)

pending = {}  # { plot_id: {pos, color} }

@app.route('/push', methods=['POST'])
def push():
    data = request.json
    pending[data['plot_id']] = data
    return 'ok'

@app.route('/poll/<plot_id>')
def poll(plot_id):
    data = pending.pop(plot_id, None)
    return jsonify(data or {})

app.run(host='0.0.0.0', port=8080)
