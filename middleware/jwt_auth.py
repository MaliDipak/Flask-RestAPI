import mysql.connector
import json
import random
from flask import make_response, jsonify, send_file, request
from datetime import datetime, timedelta
import jwt
import re
import ast
from functools import wraps

class JWT_Auth:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="radheradhe", database="tset2")
            self.cur = self.con.cursor(dictionary=True)
            print('Connection successful')
        except Exception as e:
            print("Some error: ", e)


    def token_auth(self,endpoint=""):
        def inner1(func):

            @wraps(func)

            def inner2(*args):

                endpoint = request.url_rule
                

                Authorization_token = request.headers.get("Authorization")
                
                if re.match("^Bearer *([^ ]+) *$", Authorization_token, flags=0):
                    token = Authorization_token.split(" ").pop()

                    try:
                        auth_user_data = jwt.decode(token, "hello", algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response(make_response({"ERROR":"TOKEN_EXPIRED"}, 401))
                    
                    
                    role_id = auth_user_data["payload"]["role_id"]

                    self.cur.execute(f"select roles from accessibility_view where endpoint = '{endpoint}'")
                   
                    res = self.cur.fetchall()
                    
                    if len(res)>0:

                        roles = res[0]["roles"]

                        # roles = ast.literal_eval(roles)


                        if role_id in json.loads(roles):

                            return func(*args)
                        else:
                            return make_response({"ERROR":"INVALID_ROLE"}, 401)
        
            
                    
                    else:
                        return make_response({"ERROR":"end point not found"}, 401)
        

                    
                else:
                    return make_response({"ERROR":"Invalid Token"}, 401)
            
            return inner2
        
        return inner1
        
 