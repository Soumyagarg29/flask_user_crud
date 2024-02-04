import flask
from flask import Flask, request, jsonify
from app import app
from dao import user_model
import os
from datetime import datetime
from services.user_services import UserService
from utils.logger import log_request    

# Create an instance of UserService
user_service_instance = UserService()

class UserController:
    @staticmethod
    @app.route("/")
    def default():
        return "Welcome to User Management System"

    @staticmethod
    @app.route("/user/all" , methods=["GET"])
    @log_request("/user/all")
    def get_all_user_controller():
        try:
            user = user_service_instance.get_all_user_service()
            return jsonify(user)
        except Exception as e:
            print("HERE")
            return str(e)

    @staticmethod
    @app.route("/user/add", methods=["POST"])
    @log_request("/user/add")
    def add_user_controller():
        return user_service_instance.add_user_service(request.json)

    @staticmethod
    @app.route("/user/addmultiple", methods=["POST"])
    @log_request("/user/addmultiple")
    def add_multiple_users_controller():
        return user_service_instance.add_multiple_users_service(request.json)

    @staticmethod
    @app.route("/user/delete/<id>", methods=["DELETE"])
    @log_request("/user/delete/<id>")
    def delete_user_controller(id):
        return user_service_instance.delete_user_service(id)

    @staticmethod
    @app.route("/user/update", methods=["PUT"])
    @log_request("/user/update")
    def update_user_controller():
        return user_service_instance.update_user_service(request.json)

    @staticmethod
    @app.route("/user/patch", methods=["PATCH"])
    @log_request("/user/patch")
    def patch_user_controller():
        return user_service_instance.patch_user_service(request.json)
