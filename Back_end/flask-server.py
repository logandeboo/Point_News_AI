from audioop import add
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
            # retrieve new article to be added to feed
            temp = json.loads(getArticleFeed("news/" + route, 1))

            # append contents of current JSON array into new JSON array, which starts with the new article
            # contents will be null upon server initialization
            if cache.get(route) is not None:
                for item in json.loads(cache.get(route)):
                    temp.append(item)

            cache.set(route, json.dumps(
                temp, default=lambda o: o.__dict__, indent=4))

        # json.loads on cache returns array
        # current = json.loads(cache.get('Environment'))
        # for item in json.loads(cache.get('Environment')):
        #     current.append(item)
        # new = addition + current
        # cache.set('Politics', new)
        # print(current)

    if __name__ == "__main__":
        # scheduler.add_job(id='Scheduled Update',
        #                   func=scheduledUpdate, trigger='interval', seconds=45)
        # scheduler.start()
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
# json.loads - json string -> python object


create_app()
