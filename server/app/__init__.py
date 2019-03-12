import os

from flask import Flask, render_template, jsonify, json, request, session, Blueprint, redirect, url_for

# Creating App

def create_app(config_name):
    app = Flask(__name__, static_folder='../../static/dist',
                template_folder='../../static')

    @app.route("/")
    def index():
        return render_template('home.html')

    return app