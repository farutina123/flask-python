from flask import Flask

app = Flask(__name__)

from agents.app import routes