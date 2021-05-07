from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from arrotechtools import Serializer
import pandas as pd
from os import path
basedir = path.abspath(path.dirname(__file__))
filepath = path.join(basedir, 'YOUR_FILE_LOCATION_INCLUDING_FILENAME')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_APP_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DATABASE_URI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """User Model."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50))
    street = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip = db.Column(db.Integer)

    def __repr__(self):
        """Print user object."""
        return "<User : {}>".format(first_name)


@app.route('/')
def readCSV():
    """Parse csv data."""
    with open(filepath, 'r') as csvfile:
        csv_data = pd.read_csv(csvfile)
        for index, row in csv_data.iterrows():
            user = User(first_name=row[0],
                        last_name=row[1],
                        address=row[2],
                        street=row[3],
                        state=row[4],
                        zip=row[5])
            db.session.add(user)
            db.session.commit()
        return "User successfully created!"


if __name__ == '__main__':
    app.run()
