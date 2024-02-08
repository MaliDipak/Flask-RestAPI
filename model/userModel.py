import mysql.connector
import json
import random
from flask import make_response, jsonify

class UserModel:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="radheradhe", database="tset2")
            self.cur = self.con.cursor(dictionary=True)
            print('Connection successful')
        except Exception as e:
            print("Some error: ", e)

    def get_all(self):
        try:
            query = "SELECT * FROM new_table"
            self.cur.execute(query)
            data = self.cur.fetchall()
            if data:
                res = make_response(jsonify({"payload": data}), 200)
                # res.headers["Access-Control-Allow-Origin"] = "*"  # CORS  now there is no need to implement it here for all the methods.
                #  it is implemented in app.py file 
                return res
            else:
                return make_response(jsonify({"message": "No data found"}), 204)
        except Exception as e:
            return make_response(jsonify({"error": f"Error fetching data: {str(e)}"}), 500)
        
    def get_one(self):
        try:
            query = "SELECT * FROM new_table"
            self.cur.execute(query)
            data = self.cur.fetchall()
            if data:
                res = make_response(json.dumps(random.choice(data)), 200)
                return res
            else:
                return make_response(jsonify({"message": "No data found"}), 204)
        except Exception as e:
            return make_response(jsonify({"error": f"Error fetching data: {str(e)}"}), 500)
        
    def get_one_by_id(self, id):
        try:
            query = f"SELECT * FROM new_table WHERE id={id}"
            self.cur.execute(query)
            data = self.cur.fetchall()
            if data:
                res = make_response(json.dumps(random.choice(data)), 200)
                return res
            else:
                return make_response(jsonify({"message": "No data found"}), 204)
        except Exception as e:
            return make_response(jsonify({"error": f"Error fetching data: {str(e)}"}), 500)
        
    def add_user(self, data):
        try:
            name = data["name"]
            query = f"INSERT INTO new_table (name) VALUES ('{name}')"
            self.cur.execute(query)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
        else:
            self.con.commit()
            return make_response(jsonify({"message": f"User {name} added"}), 201)
        
    def update_user(self, data):
        try:
            name = data["name"]
            id = data["id"]
            query = f"UPDATE new_table SET name='{name}' WHERE id={id}"
            self.cur.execute(query)
            row_affected = self.cur.rowcount
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
        else:
            self.con.commit()
            if row_affected > 0:
                return make_response(jsonify({"message": f"User {id} updated"}), 200)
            else:
                return make_response(jsonify({"message": f"User {id} not found or something went wrong!"}), 204)
    
    def update_patch_user(self, data, id):
        try:
            query_start = "UPDATE new_table SET "
            query_end = f" WHERE id={id}"

            for key, value in data.items():
                query_start += f"{key}='{value}',"

            query = query_start[:-1] + query_end

            self.cur.execute(query)
            row_affected = self.cur.rowcount
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
        else:
            self.con.commit()
            if row_affected > 0:
                return make_response(jsonify({"message": f"User {id} updated"}), 200)
            else:
                return make_response(jsonify({"message": f"User {id} not found or something went wrong!"}), 204)
    
    def delete_user(self, id):
        try:
            query = f"DELETE FROM new_table WHERE id={id}"
            self.cur.execute(query)
            row_affected = self.cur.rowcount
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
        else:
            self.con.commit()
            if row_affected > 0:
                return make_response(jsonify({"message": f"User {id} deleted"}), 200)
            else:
                return make_response(jsonify({"message": "Either user not found or no data to change"}), 204)
    
    def delete_all_users(self):
        try:
            query = "DELETE FROM new_table WHERE id > 0"
            self.cur.execute(query)
            row_affected = self.cur.rowcount
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
        else:
            self.con.commit()
            if row_affected > 0:
                return make_response(jsonify({"message": "All users deleted"}), 200)
            else:
                return make_response(jsonify({"message": "Either users not found or no data to change"}), 204)
