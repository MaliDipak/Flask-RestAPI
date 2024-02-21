import mysql.connector
import json
import random
from flask import make_response, jsonify, send_file
from datetime import datetime, timedelta
import jwt
from config.config import dbconfig

class UserModel:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=dbconfig["hostname"], user=dbconfig["username"], password=dbconfig["password"], database=dbconfig["dbname"])
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

    
    def get_all_user_pagination_model(self,limit,page):
        try:
            limit = int(limit)
            page = int(page)
            start = (page*limit)-limit
            query = f"SELECT * FROM new_table limit {start},{limit}"
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


    def avatar_model(self, file_name,uid):
        try:
            query = f"UPDATE new_table SET avatar='{file_name}' WHERE id={uid}"
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
            
    def get_avatar_model(self, file_name):
        try:
            return send_file(f"data/{file_name}")
        except Exception as e:
            return make_response(jsonify({"message": f"User {id} not found or something went wrong!"}), 204)

    
    def user_login_model(self,data):
        id = data["id"]
        # name = data["name"]
        try:
            query = f"SELECT * FROM new_table WHERE id={id}"
            self.cur.execute(query)
            data = self.cur.fetchall()
            user_data = data[0]
            exp_time = datetime.now() + timedelta(minutes=15)
            exp_epoch_time = int(exp_time.timestamp())
            secrete_key = "hello"
            payload = {
                "payload":user_data,
                "exp":exp_epoch_time
            }
            token = jwt.encode(payload, secrete_key, algorithm="HS256")

            if data:
                res = make_response({"token":token}, 200)
                return res
            else:
                return make_response(jsonify({"message": "No data found"}), 204)
        except Exception as e:
            return make_response(jsonify({"error": f"Error fetching data: {str(e)}"}), 500)
        