
import json

politicsFeed = {0: {'eventURI': '1234', 'title': 'title here',
                    'articles': {0: {'title': 'title', 'body': 'body', 'uri': 'uri'}, 1: {'title': 'title', 'body': 'body', 'uri': 'uri'}}, 'bullets': ['-b1', '-b2']},

                1: {'eventURI': '12', 'title': 'TITLE here',
                    'articles': ['article11', 'article12'], 'bullets': ['-b3', '-b4']}}


test = json.dumps(politicsFeed, default=lambda o: o.__dict__, indent=4)

print(test)

print(politicsFeed[0]['articles'][0])
politicsFeed[0]['articles'][2] = {
    'title3': 'title3', 'body3': 'body', 'test': 'test'}

print(politicsFeed[0]['articles'][2])


myDict = {'name': 'Logan'}

myDict['age'] = {0: {'title': 'title'}}

testDict = {0: {}}


testDict[1] = {1: {'test': 'test'}}

print(testDict)
