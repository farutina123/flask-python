from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

@app.route('/calc/<int:one>/<int:two>')
def calc(one, two):
    return f"The sum of {one} and {two} is {one+two}."

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)