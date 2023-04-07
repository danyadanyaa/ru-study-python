from typing import Any, Tuple

from flask import Flask, request

user_data: dict[str, dict] = dict()


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        app.add_url_rule("/user", view_func=FlaskExercise.create_user, methods=["POST"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.show_user, methods=["GET"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.update_user, methods=["PATCH"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.delete_user, methods=["DELETE"])

    @staticmethod
    def create_user() -> Tuple[dict, int]:
        username = request.json
        if "name" in username:
            user_data[username["name"]] = dict()
            return {"data": f"User {username['name']} is created!"}, 201
        return {"errors": {"name": "This field is required"}}, 422

    @staticmethod
    def show_user(name: str) -> Tuple[dict, int]:
        if name in user_data:
            return {"data": f"My name is {name}"}, 200
        return {"errors": "User not found"}, 404

    @staticmethod
    def update_user(name: str) -> Tuple[dict, int]:
        username = request.json.get("name")
        if name in user_data:
            user_data[username] = user_data[name]
            del user_data[name]
            return {"data": f"My name is {username}"}, 200
        return {"errors": "User not found"}, 404

    @staticmethod
    def delete_user(name: str) -> Tuple[Any, int]:
        if name in user_data:
            del user_data[name]
            return "", 204
        return {"errors": "User not found"}, 404
