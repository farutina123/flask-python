from flask import Flask

app = Flask(__name__)

from lesson2.app import routes
