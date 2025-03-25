from flask import Flask

app = Flask(__name__)

from form.app import routes