import openai

openai.api_key = (
    "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")

pointsDict = []


def addPoints(articleBody):

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
    print(resLines)
    print("___________________")
    # pointsDict = {1: resLines[2], 2: resLines[3], 3: resLines[4]}
    # pointsDict[0] = resLines[2]
    # pointsDict[0] = resLines[3]
    # pointsDict[0] = resLines[4]

    for item in resLines:
        if item != '':
            pointsDict.append(item[2:])

    print(pointsDict)
    return pointsDict


body = "Washington -- Senate Republicans on Sunday blocked a $35 monthly cap on the cost of insulin in the private market from being included in Democrats' economic tax and spending package, voting down an amendment to the measure during a marathon session leading up to what Democrats hope will be final passage of the bill.\n\nThe Senate on Saturday night began consideration of more than 30 amendments to the Inflation Reduction Act, Democrats' $700 billion legislation that aims to combat climate change, raise taxes on large corporations and address rising health care costs.\n\nAmid the proposed changes to the plan was to set the $35 per month cap on insulin, the pricy medication needed to treat diabetes. Seven Republican senators voted with all 50 Democrats to keep the price ceiling in the legislation: Bill Cassidy of Louisiana, Susan Collins of Maine, Josh Hawley of Missouri, Cindy Hyde Smith of Mississippi, John Kennedy of Louisiana, Lisa Murkowski of Alaska and Dan Sullivan of Alaska.\n\nStill, with a vote of 57 to 43, the provision failed to garner the 60 votes needed to waive special budgetary rules and include it in the bill. The House passed a similar cap on the price of insulin in April.\n\nDemocrats are hoping to clear their overall legislative package on Sunday, setting the House up to briefly return to Washington this week to approve it. Its passage would notch President Biden and congressional Democrats a key win before the midterm elections, when they are working to maintain control of Congress.\n\nThe legislation is the culmination of months of negotiations over Mr. Biden's domestic policy plan, which at times appeared dead but was revived late last month with the surprise announcement of an agreement between Senate Majority Leader Chuck Schumer and Sen. Joe Manchin, a moderate Democrat from West Virginia.\n\nDemocrats praise the plan as their answer to addressing inflation and its nearly $400 billion investment in fighting climate change. The package allows Medicare to negotiate prescription drug prices, extends enhanced health insurance subsidies that were set to expire at the end of the year and imposes a 15% minimum tax on corporations that make more than $1 billion each year.\n\nTo boost clean energy, the measure includes tax credits for buying electric vehicles and manufacturing solar panels and wind turbines. It also provides rebates for consumers who buy energy efficient appliances and provides $4 billion for drought relief."

addPoints(body)
