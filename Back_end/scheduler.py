#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from turtle import home
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


def run_app():

    var = 0
    app = Flask(__name__)

    @app.route("/home")
    def home():
        var + 1
        return str(var)

    sched = BackgroundScheduler()
    sched.add_job(home, 'interval', seconds=5)
    sched.start()

    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=5002)


run_app()
