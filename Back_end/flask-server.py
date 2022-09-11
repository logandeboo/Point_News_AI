import json
from flask import Flask
from flask_caching import Cache
from flask import Flask
from article_feed import getArticleFeed
from waitress import serve
from flask_apscheduler import APScheduler


business = 'news/Business'
politics = 'news/Politics'
health = 'news/Health'
arts_and_entertainment = 'news/Arts_and_Entertainment'
science = 'news/Science'
sports = 'news/sports'
technology = 'news/Technology'
environment = 'news/Environment'
seconds_in_day = 86400


cache = Cache(config={"CACHE_TYPE": "RedisCache",
                      "CACHE_REDIS_HOST": "0.0.0.0",
                      "CACHE_REDIS_PORT": 6379,
                      "CACHE_DEFAULT_TIMEOUT": -1})


def create_app():

    # TODO
    # Write new logic to control when articles get added
    # Refactor to remove duplicate code

    app = Flask(__name__)
    cache.init_app(app)
    scheduler = APScheduler()

    @app.route('/Politics')
    def post_politics():
        print("politics routed")
        if cache.get('Politics') is None:
            cache.set('Politics', getArticleFeed(politics, 2))
        return cache.get("Politics")

    @app.route('/Business')
    def post_Business():
        if cache.get('Business') is None:
            cache.set('Business', getArticleFeed(business, 0))
        return cache.get("Business")

    @app.route('/Health')
    def post_Health():
        if cache.get('Health') is None:
            cache.set('Health', getArticleFeed(health, 0))
        return cache.get("Health")

    @app.route('/Entertainment')
    def post_Entertainment():
        if cache.get('Entertainment') is None:
            cache.set('Entertainment', getArticleFeed(
                arts_and_entertainment, 0))
        return cache.get("Entertainment")

    @app.route('/Science')
    def post_Science():
        if cache.get('Science') is None:
            cache.set('Science', getArticleFeed(science, 0))
        return cache.get("Science")

    @app.route('/Technology')
    def post_Technology():
        if cache.get('Technology') is None:
            cache.set('Technology', getArticleFeed(technology, 0))
        return cache.get("Technology")

    @app.route('/Environment')
    def post_Environment():
        if cache.get('Environment') is None:
            cache.set('Environment', getArticleFeed(environment, 0))
        return cache.get("Test")

    @app.route('/Test')
    def test():
        return cache.get("Test")

    def scheduledTask(route_name):
        temp = []
        temp = json.loads(getArticleFeed(politics, 1))
        temp.append(json.loads(cache.get("Politics")))
        cache.set(route_name, json.dumps(
            temp, default=lambda o: o.__dict__, indent=4))

    if __name__ == "__main__":
        # scheduler.add_job(id='Scheduled task',
        #                   func=scheduledTask, trigger='interval', seconds=25)
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
# json.loads - json string -> python dict

def update_articles():
    print(cache.get('Business'))


create_app()
