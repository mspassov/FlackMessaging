import os
import requests

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
	username = request.form.get("user")
	channel = request.form.get("channel")
	return render_template("room.html", username=username, channel=channel)

@socketio.on('joined_room')
def joinEvent(data):
	join_room(data['channel'])
	socketio.emit('new_user_announce', data)


if __name__ == "__main__":
	app.run(debug=True)