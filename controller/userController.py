from app import app
from model.userModel import UserModel
from middleware.jwt_auth import JWT_Auth
from flask import request, make_response, jsonify
from datetime import datetime

obj = UserModel()
auth = JWT_Auth()

@app.route("/test")
def test():
    return "test"


@app.route("/user/getall")
@auth.token_auth()
def get_all_route():
    try:
        response = obj.get_all()
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/getone")
@auth.token_auth()
def get_one_route():
    try:
        response = obj.get_one()
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/getone/<id>")
def get_one_by_id_route(id):
    try:
        response = obj.get_one_by_id(id)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/add", methods=["POST"])
def add_user_route():
    try:
        data = request.form
        response = obj.add_user(data)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/update", methods=["PUT"])
def update_user_route():
    try:
        data = request.form
        response = obj.update_user(data)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
        

@app.route("/user/updatepatch/<id>", methods=["PATCH"])
def update_patch_route(id):
    try:
        data = request.form
        response = obj.update_patch_user(data, id)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

    

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user_route(id):
    try:
        response = obj.delete_user(id)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/deleteall", methods=["DELETE"])
def delete_all_users_route():
    try:
        response = obj.delete_all_users()
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)


@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def get_all_users_by_limit_route(limit,page):
    try:
        response = obj.get_all_user_pagination_model(limit,page)
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    

@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def user_avatar_route(uid):
    file = request.files['avatar']
    unique_name = str(datetime.now().timestamp()).replace(".","")
    file_extension = file.filename.split(".").pop()
    file_name = f"{unique_name}.{file_extension}"
    file.save(f"data/{file_name}")
    try:
        response = obj.avatar_model(file_name,uid)
        return response
    except Exception as e:
        return  make_response(jsonify({"error": str(e)}), 500)


@app.route("/user/avatar/<filename>",methods=["GET"])
def user_get_avatar_route(filename):
    try:
        response = obj.get_avatar_model(filename)
    except Exception as e:
        return  make_response(jsonify({"error": str(e)}), 500)
    else:
        return response
    

@app.route("/user/login", methods=["POST"])
def user_login_route():
    data = request.form
    try:
        response = obj.user_login_model(data)
    except Exception as e:
        return  make_response(jsonify({"error": str(e)}), 500)
    else:
        return response