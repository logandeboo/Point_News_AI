import openai
import credentials

openai.api_key = (
    credentials.gpt_key)


def addPoints(articleBody):
    points = []
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Summarize this into 3 bullet points for a college student:\n" +
        articleBody,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    resLines = str.splitlines(response['choices'][0]['text'])
    for item in resLines:
        if item != '':
            points.append(item[1:])
    return points
