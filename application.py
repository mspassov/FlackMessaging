import os
import requests
import json

from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
#app.secret_key = "asdfasdfas"

currentUsers = []
currentChannels = []

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/chats", methods=["POST"])
def chats():
	username = request.form.get("user")
	#session['username'] = username;

	currentUsers.append(username)
	return render_template("chats.html", username=username, currentChannels=json.dumps(currentChannels))

@app.route("/channels/<string:user>/<string:chan>")
def channelRoom(user, chan):
	return render_template('room.html', channel=chan, username=user)

@socketio.on('update_channels')
def update_channels(data):
	currentChannels.append(data['channel'])
	socketio.emit('display_channels', currentChannels)

@socketio.on('joined_room')
def joinEvent(data):
	join_room(data['channel'])
	socketio.emit('new_user_announce', data, room=data['channel'])

@socketio.on('sent_message')
def sendMessage(data):
	socketio.emit('receiveMessage', data, room=data['channel'])

if __name__ == "__main__":
	app.run(debug=True)