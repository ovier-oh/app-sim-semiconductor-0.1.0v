from flask import Flask, request, jsonify
from app.models import db, User 
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)

@app.before_first_request 
def create_tables():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    data = request.json 
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username),first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful"}), 200 
    else:
        return jsonify({"message": "Invalid credentials"}), 401 

if __name__ == '__main__':
    app.run(debug=True)
    