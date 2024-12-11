from app import app
from flask import Flask, request, redirect, url_for, render_template, jsonify
from app.db import get, create


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/api/users', methods=['GET'])
def get_users():
    return get()


@app.route('/api/add-user', methods=['POST'])
def add_user():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    create(request.get_json())
    return 'User Added'
