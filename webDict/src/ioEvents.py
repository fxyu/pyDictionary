from flask import Flask, request
from flask_socketio import SocketIO, send, emit

import json

def socketIOEvents(socketio, db):
#====== DEFAULT EVENT ==============
    @socketio.on('message')
    def handle_message(msg):
        print(msg)

    @socketio.on('json')
    def handle_json(json):
        print(json)

    @socketio.on('connect')
    def handle_new_connection():
        print('A user connected')

    @socketio.on('disconnect')
    def handle_new_connection():
        print('A user disconnected')

#======= webDict EVENT ==============
    @socketio.on('client_searchWord')
    def searchWord(word):
        print('Search word : {}'.format(word))
        x = db.get(word)
        socketio.emit('server_newWord', (word, x), broadcast=True)

    @socketio.on('client_getHistory')
    def getHistory(x):
        print('client getHistory')
        x = db.getHistory()
        return x



