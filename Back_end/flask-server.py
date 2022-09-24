import json
from flask import Flask
from flask_caching import Cache
from flask import Flask
from article_feed import getArticleFeed
from flask_apscheduler import APScheduler


routes = ['Politics', 'Business', 'Health',
          'Entertainment', 'Science', 'Technology', 'Environment']

seconds_in_day = 86400


cache = Cache(config={"CACHE_TYPE": "RedisCache",
                      "CACHE_REDIS_HOST": "0.0.0.0",
                      "CACHE_REDIS_PORT": 6379,
                      "CACHE_DEFAULT_TIMEOUT": -1})


def create_app():

    app = Flask(__name__)
    cache.init_app(app)
    scheduler = APScheduler()

    # Route pages will be empty upon initialization of cloud instance
    # Empty checks and cahce setting handle the first instance of this

    @app.route('/Politics')
    def get_politics():
        if cache.get("Politics") is None:
            cache.set("Politics", getArticleFeed("news/Politics", 8))
        return cache.get("Politics")

    @app.route('/Business')
    def get_Business():
        if cache.get("Business") is None:
            cache.set("Business", getArticleFeed("news/Business", 8))
        return cache.get("Business")

    @app.route('/Health')
    def get_Health():
        if cache.get("Health") is None:
            cache.set("Health", getArticleFeed("news/Health", 8))
        return cache.get("Health")

    @app.route('/Entertainment')
    def get_Entertainment():
        if cache.get("Entertainment") is None:
            cache.set("Entertainment", getArticleFeed(
                "news/Arts_and_Entertainment", 8))
        return cache.get("Entertainment")

    @app.route('/Science')
    def get_Science():
        if cache.get("Science") is None:
            cache.set("Science", getArticleFeed("news/Science", 8))
        return cache.get("Science")

    @app.route('/Technology')
    def get_Technology():
        if cache.get("Technology") is None:
            cache.set("Technology", getArticleFeed("news/Technology", 8))
        return cache.get("Technology")

    @app.route('/Environment')
    def get_Environment():
        if cache.get("Environment") is None:
            cache.set("Environment", getArticleFeed("news/Environment", 8))
        return cache.get("Environment")

    def scheduledUpdate():
        for route in routes:
            # retrieve new article to be added to feed
            temp = json.loads(getArticleFeed("news/" + route, 2))
            # append contents of current JSON array into new JSON array, which starts with the new article
            for item in json.loads(cache.get(route)):
                temp.append(item)

            cache.set(route, json.dumps(
                temp, default=lambda o: o.__dict__, indent=4))

    if __name__ == "__main__":
        scheduler.add_job(id='Scheduled Update',
                          func=scheduledUpdate, trigger='interval', seconds=seconds_in_day)
        scheduler.start()
        app.run(debug=False, host="0.0.0.0", port=5001)


create_app()
