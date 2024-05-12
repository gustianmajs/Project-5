from flask import Flask, jsonify, request
from decouple import config
import psycopg2
from flask_sqlalchemy import SQLAlchemy


DB_URI = f"postgresql+psycopg2://{config('MB_DB_USER')}:{config('MB_DB_PASS')}@{config('MB_DB_HOST')}:{config('MB_DB_PORT')}/{config('MB_DB_DBNAME')}"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    telp = db.Column(db.String(114))



@app.route('/health')
def health():
    return jsonify({"status": "UP"})

@app.route('/db_check')
def db_check():
    try:
        conn_pg = psycopg2.connect(
            host=config('MB_DB_HOST'),
            database=config('MB_DB_DBNAME'),
            user=config('MB_DB_USER'),
            password=config('MB_DB_PASS'),
            port=config('MB_DB_PORT')
        )
        cur = conn_pg.cursor()
        return jsonify({"status": 200, "db": "DB Connection Successful"})

    except Exception as e:
        return jsonify({"status": 500, "error": str(e)})


@app.route("/user", methods=["GET", "POST", "PUT", "DELETE"])
def user():
    if request.method == "GET":
        users = Users.query.all()
        results = [{"id": u.id, "name": u.name, "city": u.city, "telp": u.telp} for u in users]
        return jsonify(results)

    elif request.method == "POST":
        user = Users(
            name=request.form["name"], 
            city=request.form["city"], 
            telp=request.form["telp"]
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"status": "Added, OK"})

    elif request.method == "PUT":
        user.name = request.form["name"]
        user.city = request.form["city"]
        user.telp = request.form["telp"]
        db.session.commit()
        return jsonify({"status": "Change, OK"})

    elif request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return jsonify({"status": "Delete, OK"})

    else:
        return jsonify({"status": 405})

@app.route("/user/<int:id>", methods=["GET"])
def user_id(id):
    user = Users.query.filter_by(id=id).first()
    try:
        result = {"id": user.id, "name": user.name, "city": user.city, "telp": user.telp}
        return jsonify(result)
    except:
        return jsonify({"status": 404})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
