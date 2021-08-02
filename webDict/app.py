from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

from src.ioEvents import socketIOEvents
from src.dict_db import dict_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsAVerySecretStringThatIWillNotBeAbleToDecrypt!'
socketio = SocketIO(app)
db = dict_db()

# simple routing
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search/<word>', methods=['GET'])
def search(word):
    print('Search from get method (word : {})'.format(word))
    socketio.emit('server_newWord', (word, db.get(word)), broadcast=True)
    return 'submitted'


@app.route('/playAudio', methods=['GET'])
def playAudio():
    socketio.emit('server_playAudio', (), broadcast=True)
    return 'played'

# @app.route('/new')
# def new():
#     data = {
#         'array':list(range(16)),
#         'title':"Testing"
#     }
#     socketio.emit('cNewMatrix', data)
#     return "Sent"

events = socketIOEvents(socketio, db)

if __name__ == "__main__":
    # app.run(port=5000)
    print("Start Server!")
    socketio.run(app, host="0.0.0.0", debug=True, port=5001)
    