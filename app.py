import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Production Best Practice: Use environment variable for the database.
database_uri = os.environ.get('POSTGRES_URL') or os.environ.get('DATABASE_URL')

if database_uri and database_uri.startswith("postgres://"):
    # Fix for older PostgreSQL URIs (SQLAlchemy 1.4+ requires postgresql://)
    database_uri = database_uri.replace("postgres://", "postgresql://", 1)
elif not database_uri:
    # On Vercel, the filesystem is read-only except for /tmp.
    if os.environ.get('VERCEL'):
        database_uri = 'sqlite:////tmp/db.sqlite'
    else:
        # Fallback to local SQLite database for local development.
        database_uri = 'sqlite:///db.sqlite'

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Ensure tables are created when the application starts
# This is necessary for serverless environments like Vercel where __main__ does not run
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
