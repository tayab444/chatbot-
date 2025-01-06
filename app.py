from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

openai.api_key = "AIzaSyBv-SchWmbGSNeM6wIVEESwb0t7s9UPDTY"

from models import User, Conversation

@app.route('/register', methods=['POST'])
def register():
    ...

@app.route('/chat', methods=['POST'])
def chat():
    ...

if __name__ == "__main__":
    app.run(debug=True)
