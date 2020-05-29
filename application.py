import os
import requests

from flask import Flask, render_template, jsonify, request, session
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.secret_key = "asdfasdfas"

currentUsers = []
currentChannels = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chats", methods=["POST"])
def chats():
	username = request.form.get("user")
	session['username'] = username;

	if username in currentUsers:
		return "username already taken"
	else:
		currentUsers.append(username)
		return render_template("chats.html", username=username)

@app.route("/channels/<string:chan>")
def channelRoom(chan):
	return render_template('room.html', channel=chan, username=session['username'])

@socketio.on('update_channels')
def update_channels(data):
	socketio.emit('display_channels', data)

@socketio.on('joined_room')
def joinEvent(data):
	join_room(data['channel'])
	socketio.emit('new_user_announce', data)

@socketio.on('sent_message')
def sendMessage(data):
	socketio.emit('receiveMessage', data, room=data['channel'])


if __name__ == "__main__":
	app.run(debug=True)