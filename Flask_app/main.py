from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD=True
)

client = MongoClient("mongodb://mongo-container:27017")

db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html',todos=all_todos)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
