from flask import Flask, jsonify
import datetime

app = Flask(__name__)
k = 0

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def increment_counter():
    global k
    k += 1

@app.route('/time', methods=['GET'])
def time_endpoint():
    increment_counter()
    return jsonify({'current_time': get_current_time(), 'requests_count': k})

@app.route('/statistics', methods=['GET'])
def statistics_endpoint():
    return jsonify({'total_requests': k})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
