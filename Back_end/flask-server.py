import json
from flask import Flask
from flask_caching import Cache
from flask import Flask
from article_feed import getArticleFeed
from flask_apscheduler import APScheduler


# routes = ['Politics', 'Business', 'Health',
#           'Entertainment', 'Science', 'Technology', 'Environment']

routes = ['Politics']


seconds_in_day = 86400


cache = Cache(config={"CACHE_TYPE": "RedisCache",
                      "CACHE_REDIS_HOST": "0.0.0.0",
                      "CACHE_REDIS_PORT": 6379,
                      "CACHE_DEFAULT_TIMEOUT": -1})


def create_app():

    app = Flask(__name__)
    cache.init_app(app)
    scheduler = APScheduler()

    @app.route('/Politics')
    def get_politics():
        print("Politics route hit")
        return cache.get("Politics")

    @app.route('/Business')
    def get_Business():
        return cache.get("Business")

    @app.route('/Health')
    def get_Health():
        return cache.get("Health")

    @app.route('/Entertainment')
    def get_Entertainment():
        return cache.get("Entertainment")

    @app.route('/Science')
    def get_Science():
        return cache.get("Science")

    @app.route('/Technology')
    def get_Technology():
        return cache.get("Technology")

    @app.route('/Environment')
    def get_Environment():
        return cache.get("Environment")

    def scheduledUpdate():
        print("Updating")
        for route in routes:
            temp = []
            temp = json.loads(getArticleFeed("news/" + route, 1))

            if cache.get(route) is not None:
                temp + json.loads(cache.get(route))

            cache.set(route, json.dumps(
                temp, default=lambda o: o.__dict__, indent=4))

    if __name__ == "__main__":
        scheduler.add_job(id='Scheduled Update',
                          func=scheduledUpdate, trigger='interval', seconds=20)
        scheduler.start()
        app.run(debug=False, host="0.0.0.0", port=5001)


# Testing update method
# There should be a scheduled update method that does the "putting"
# The routes should exclusively be "getting"
# --------------------------------------------
# TODO:
# - Write method to update cache
# - Use APScheduler to schedule said method
# REMEMBER TO CHANGE REDIS HOST AFTER TESTING

# TODO Updated
# - No 'update' strategy is present in rediscache operators Sooo..
# The solution is to get the route dictionary, append an new article(s) to it, then set the updated value
# json.dumps - python object -> json string
# json.loads - json string -> python dict


create_app()
