from flask_cors import CORS
from flask import request, Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit
import eventlet
import datetime

eventlet.monkey_patch(socket=True, select=True)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# socket = SocketIO(application, async_mode='gevent', ping_timeout=30, logger=False, engineio_logger=False)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')
clients = []
clientDict = []

@app.route("/")
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    print('page not found')
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/clients")
def get_clients():
    print()
    print(clients)
    print()
    return jsonify(message="dummy", clients=clients, dict=clientDict), 200

@socketio.on('connect')
def connect():
    print("%s connected" % (request.sid))
    clients.append(request.sid)
    cd = {'sid': request.sid, 'userName': 'unknown'}
    clientDict.append(cd)
    # emit('room', {'message': 'Hello there client', 'clientId': request.sid})


@socketio.on('disconnect')
def disconnect():
    print("%s has disconnected" % (request.sid))
    clients.remove(request.sid)
    userName = getClientName(request.sid)
    removeClient(request.sid)
    update_clients()
    now = datetime.datetime.now()
    nowString = now.strftime('%Y-%m-%d %I:%M:%S %p')
    # print(nowString)
    emit('i-room', {'message': '%s has left the chat' % userName,  'userName': userName, 'currentTime': nowString}, broadcast=True)

def update_clients():
    activeClients = [c['userName'] for c in clientDict]
    emit('clients', {'clients': activeClients}, broadcast=True)

@socketio.on('room')
def room_connect(d):
    print(d)
    addClientName(request.sid, d["userName"])
    sid = request.sid
    print(sid)
    update_clients()
    emit('i-room', {'message': d["message"],  'userName': d["userName"], 'currentTime': d["currentTime"]}, broadcast=True)


def removeClient(clientSid):
    for x in clientDict:
        if clientSid == x["sid"]:
            clientDict.remove(x)
            break

def addClientName(clientSid, userName):
    for x in clientDict:
        if clientSid == x["sid"]:
            x["userName"] = userName
            break

def getClientName(clientSid):
    for x in clientDict:
        if clientSid == x["sid"]:
            return x["userName"]
    return 'unknown'

if __name__ == '__main__':
    print('app running on http://localhost:5100/')
    # socketio.run(app, debug=True)
    socketio.run(app, host='0.0.0.0', debug=True, port=5100)
    # socketio.run()
