from flask import Flask, jsonify
import requests

app = Flask(__name__)
k = 0

def get_current_time():
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    if response.status_code == 200:
        return response.json()['datetime']
    else:
        return None

def increment_counter():
    global k
    k += 1

@app.route('/time', methods=['GET'])
def get_time():
    global k
    increment_counter()
    
    current_time = get_current_time()
    if current_time:
        return jsonify({'current_time': current_time, 'requests_count': k})
    else:
        return jsonify({'error': 'Failed to get current time'}), 555

@app.route('/statistics', methods=['GET'])
def get_statistics():
    global k
    return jsonify({'total_requests': k})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

