from flask import Flask, jsonify # type: ignore
import datetime
import socket


app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now(),
        'message': 'Example message!!!',
        'deploy_on': 'Kubernetes'
    })


@app.route('/api/v1/health')
def health():
    return jsonify({
        'status': "Working"
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
