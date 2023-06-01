from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost/customer_test'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add_user/<name>/<email>')
def add_user(name, email):
    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()
    return 'User added successfully!'


@app.route('/users')
def get_users():
    users = User.query.all()
    user_list = ""
    for user in users:
        user_list += f"Name: {user.name}, Email: {user.email}<br>"
    return user_list


if __name__ == '__main__':
    app.run(debug=True)
