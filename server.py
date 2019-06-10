from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    query = "INSERT INTO Pets (name, type, created_at, updated_at) VALUES (%(pn)s, %(pt)s, NOW(), NOW());"
    data = {
        "pn" : request.form['pet_name'],
        "pt" : request.form['pet_type']
    }
    db = connectToMySQL('pets')
    db.query_db(query, data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)