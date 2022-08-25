from flask import Flask
from flask_caching import Cache
from flask import Flask
from article_feed import getArticleFeed


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

    app = Flask(__name__)
    cache.init_app(app)

    @app.route('/Politics')
    def post_politics():
        if cache.get('Politics') is None:
            cache.set('Politics', getArticleFeed(politics, 4))
        return cache.get("Politics")

    @app.route('/Business')
    def post_Business():
        if cache.get('Business') is None:
            cache.set('Business', getArticleFeed(business, 4))
        return cache.get("Business")

    @app.route('/Health')
    def post_Health():
        if cache.get('Health') is None:
            cache.set('Health', getArticleFeed(health, 4))
        return cache.get("Health")

    @app.route('/Entertainment')
    def post_Entertainment():
        if cache.get('Entertainment') is None:
            cache.set('Entertainment', getArticleFeed(
                arts_and_entertainment, 4))
        return cache.get("Entertainment")

    @app.route('/Science')
    def post_Science():
        if cache.get('Science') is None:
            cache.set('Science', getArticleFeed(science, 4))
        return cache.get("Science")

    @app.route('/Technology')
    def post_Technology():
        if cache.get('Technology') is None:
            cache.set('Technology', getArticleFeed(technology, 4))
        return cache.get("Technology")

    @app.route('/Environment')
    def post_Environment():
        if cache.get('Environment') is None:
            cache.set('Environment', getArticleFeed(environment, 4))
        return cache.get("Environment")

    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=5001)


create_app()
