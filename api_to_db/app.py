from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///apidata.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ApiData(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    col1 = db.Column(db.String(200), nullable=False)
    col2 = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def get_from_api():
    ApiData.query.delete()
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    for key, value in data.items():
        col1 = key
        if isinstance(value, dict):
            col2 = json.dumps(value)
        else:
            col2 = value
        todo = ApiData(col1=col1, col2=col2)
        db.session.add(todo)
        db.session.commit()

    apiData = ApiData.query.all()
    return render_template('index.html', apiData=apiData)


if __name__ == "__main__":

    app.run(debug=True, port=8001)
