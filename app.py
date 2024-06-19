from flask import Flask, request, jsonify
from db import Database

app = Flask(__name__)
db = Database()  # Initialize your database connection

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    leader_name = request.form.get('leader')

    # Example: Store user data in the database
    user_id = db.add_user(email, password, leader_name)

    if user_id:
        return jsonify({'message': 'Signup successful', 'user_id': user_id}), 200
    else:
        return jsonify({'error': 'Failed to signup'}), 500

if __name__ == '__main__':
    app.run(debug=True)
