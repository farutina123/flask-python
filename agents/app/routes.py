from flask import Flask, render_template, request, redirect, url_for
from agents.app import app
from flask_sqlalchemy import SQLAlchemy
import random
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PATH_DB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(12), nullable=False)
    level = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f"<Task {self.secret_name}>"


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/secret_agents', methods=['GET', 'POST'])
def get_agents():
    secret_agents = Agent.query.all()  # Получаем все задачи из базы
    if request.method == 'POST':
        str_search = request.form['search']
        filter_agents = Agent.query.filter(Agent.secret_name.like(f'{str_search}%')).all()
        return render_template('secret_agents.html', secret_agents=filter_agents)
    return render_template('secret_agents.html', secret_agents=secret_agents)


@app.route('/add', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        name = request.form['secret_name']
        phone = request.form['phone']
        email = request.form['email']
        level = request.form['level']
        new_agent = Agent(secret_name=name, phone=phone, email=email, level=level)
        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('add.html')


@app.route('/rand')
def add_rand(): #не дает написать имя файла, только через абсолютный путь, почему так?
    with open('C:/Users/Полина/PycharmProjects/flask-python/agents/app/adjectives.txt', 'r', encoding='utf8') as one:
        arr1 = []
        for line in one:
            arr1.append(line)
    with open("C:/Users/Полина/PycharmProjects/flask-python/agents/app/nouns.txt", "r", encoding='utf8') as second:
        arr2 = []
        for i in second:
            arr2.append(i)
    random_item_first = random.choice(arr1)
    random_item_second = random.choice(arr2)
    result = f"{random_item_first} {random_item_second}"
    return render_template('add.html', rand = result)


@app.route('/agent/<int:id>')
def get_agent(id):
    agent = Agent.query.get_or_404(id)
    return render_template('agent-item.html', agent=agent)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == 'POST':
        new_name = request.form['secret_name']
        new_phone = request.form['phone']
        new_email = request.form['email']
        new_level = request.form['level']
        agent.secret_name = new_name
        agent.phone = new_phone
        agent.email = new_email
        agent.level = new_level
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('agent-edit.html', agent=agent)


@app.route('/delete/<int:id>')
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('get_agents'))


@app.route('/delete_all')
def delete_all():
    Agent.query.filter(not(Agent.secret_name == "")).delete()
    db.session.commit()
    return get_agents()