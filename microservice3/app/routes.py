from flask import request, jsonify
from app import app, property
# from mysql.connector import connect

# engine = connect(**property)
# connection = engine.cursor()



@app.route("/students" , methods=["GET","POST"])
def students():
    return "Hola"

# 	if request.method == "GET":
# 		cursor = connection.execute("SELECT * FROM students")
# 		students = [
# 		  dict(id = row[0], firstname = row[1], lastname = row[2], gender = row[3] , age = row[4])
# 		  for row in cursor.fetchall()
# 		]

# 		if students is not None:
# 			return jsonify(students)

# 	if request.method == "POST":
# 		firstname = request.form["firstname"]
# 		lastname = request.form["lastname"]
# 		gender = request.form["gender"]
# 		age  = request.form["age"]
# 		#SQL  query to INSERT a student INTO our database

# 		query = """INSERT INTO students (firstname, lastname, gender, age)
# 				 VALUES (?, ?, ?, ?) """

# 		cursor = connection.execute(query, (firstname, lastname, gender, age))

# 		return f"Student with id: {cursor.lastrowid} created successfully"

# #a route with all the neccesary request methods for a single student	
# @app.route('/student/<int:id>',methods=[ "GET", "PUT", "DELETE" ])
# def student(id):

# #createing our GET request for a student
# 	if request.method == "GET":
# 		connection.execute("SELECT * FROM students WHERE id=?",(id,) )
# 		rows = connection.fetchall()
# 		for row in rows:
# 			student = row
# 		if student is not None:
# 			return jsonify(student), 200
# 		else:
# 			return "Something went wrong", 404

# #createing our PUT request for a student
# 	if request.method == "PUT":
# 		sql = """ UPDATE students SET firstname = ?,lastname = ?, gender = ? , age = ?
# 				  WHERE id = ? """

# 		firstname = request.form["firstname"]
# 		lastname = request.form["lastname"]
# 		gender = request.form["gender"]
# 		age = request.form["age"]

# 		updated_student = {
# 			"id": id,
# 			"firstname": firstname,
# 			"lastname" : lastname,
# 			"gender" : gender,
# 			"age" : age
# 		}

# 		connection.execute(sql,(firstname, lastname, gender, age, id))
# 		connection.commit()
# 		return jsonify(updated_student)

# #createing our DELETE request for a student
# 	if request.method == "DELETE":
# 		sql= """ DELETE FROM students WHERE id=? """
# 		connection.execute(sql, (id,))
# 		connection.commit()

# 		return "The Student with id: {} has been deleted.".format(id),200
