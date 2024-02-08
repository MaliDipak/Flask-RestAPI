from app import app
from model.userModel import UserModel
from flask import request, make_response, jsonify

obj = UserModel()

@app.route("/test")
def test():
    return "test"

@app.route("/user/getall")
def get_all_route():
    try:
        response = obj.get_all()
        return response
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/user/getone")
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
