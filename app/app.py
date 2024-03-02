from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:Root123@db:5432/db_demo'
db = SQLAlchemy(app)

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

@app.route('/cars', methods=['GET'])
def get_api():
    cars = Car.query.all()
    car_list = [{'id': car.id, 'brand': car.brand, 'model': car.model, 'year': car.year} for car in cars]
    return {'cars': car_list}

if __name__ == '__main__':
    app.run(debug=True)