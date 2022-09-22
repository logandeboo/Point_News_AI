from email.quoprimime import body_check
from os import times
from eventregistry import *
from gpt import *
from datetime import datetime, timedelta
import credentials


er = EventRegistry(apiKey=credentials.news_key)
now = datetime.today()
pastWeek = now - timedelta(days=7)
pastWeek = pastWeek.strftime('%Y-%m-%d')
sources = ["news.yahoo.com", "cbsnews.com", "cnn.com", "nytimes.com", "nbcnews.com", "foxnews.com", "cnbc.com", "forbes.com", "washingtonpost.com", "reuters.com", "msnbc.com", "buzzfeednews.com", "buzzfeed.com", "npr.org", "huffingtonpost.com",
           "businessinsider.com", "politico.com", "bloomberg.com", "today.com", "foxbusiness.com", "nypost.com", "thehill.com", "thehillnews.org", "latimes.com", "theverge.com"]


def getArticleFeed(category, num_articles):
    print("getArticleFeedCalled", num_articles)
    feed = []
    q = QueryArticlesIter(categoryUri=category,
                          sourceUri=QueryItems.OR(sources),
                          locationUri="http://en.wikipedia.org/wiki/United_States",
                          lang="eng", dateStart=pastWeek)

    # change the way articles are sorted (by date)
    # filter for duplicates

    for i, ar in enumerate(q.execQuery(er, sortBy='date', maxItems=10)):

        temp = ar['body']
        word_count = len(temp.split())

        if i < num_articles:

            # if word count is too large then skip this article and take one additional from the 10 returned
            if word_count < 2500:

                feed.append({
                    'articleTitle': ar['title'],
                    'articlePoints': addPoints(ar['body']),
                    'articleDate': ar['date'],
                    'articleUrl': ar['url'],
                    'articleImg': ar['image'],
                    'articleSource': ar['source']})
            else:
                num_articles = num_articles + 1

    return json.dumps(feed, default=lambda o: o.__dict__, indent=4)
