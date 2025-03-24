from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)