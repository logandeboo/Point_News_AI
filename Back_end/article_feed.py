from hashlib import new
from eventregistry import *
from gpt import *
from datetime import datetime, timedelta
import credentials


er = EventRegistry(apiKey=credentials.news_key)
now = datetime.today()
pastWeek = now - timedelta(days=7)
pastWeek = pastWeek.strftime('%Y-%m-%d')
sources = ["news.yahoo.com", "cbsnews.com", "cnn.com", "nytimes.com", "nbcnews.com", "foxnews.com", "cnbc.com", "forbes.com", "washingtonpost.com", "reuters.com", "msnbc.com", "buzzfeednews.com", "buzzfeed.com", "npr.org", "huffingtonpost.com",
           "businessinsider.com", "politico.com", "bloomberg.com", "today.com", "foxbusiness.com", "nypost.com", "thehill.com", "thehillnews.org", "latimes.com", "hosted.ap.org", "breitbart.com", "wallstreet-online.de", "theverge.com"]


def getArticleFeed(category, num_articles):
    print("getArticleFeedCalled")
    feed = []
    q = QueryArticlesIter(categoryUri=category,
                          sourceUri=QueryItems.OR(sources),
                          locationUri="http://en.wikipedia.org/wiki/United_States",
                          lang="eng", dateStart=pastWeek)

    for i, ar in enumerate(q.execQuery(er, sortBy='socialScore', maxItems=num_articles)):
        feed.append({
            'articleTitle': ar['title'],
            'articlePoints': addPoints(ar['body']),
            'articleDate': ar['date'],
            'articleUrl': ar['url'],
            'articleImg': ar['image'],
            'articleSource': ar['source']})

    return json.dumps(feed, default=lambda o: o.__dict__, indent=4)

    # json.dumps - python object -> json string
    # json.loads - json string -> python dict
