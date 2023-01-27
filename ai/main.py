'''
TODO: Test both fliter_response() and article-topic.txt function.
TODO: Add log in ai folder to log events from ai.py to.
TODO: Add a way to automate the topic making process.
TODO: Implement timer function to activate the writer at a certain time
TODO: Add a topic header above the article that contains the topic.
TODO: Test all log functions
'''

# Imports
import os
import random
import time
import datetime
import openai

# Load API key
openai.api_key = "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"

# Variables
idea = getIdea()
topics = [
    'The 2020 Election',
    'The decline of the metaverse',
    'Crypto Scams',
    'The rise of AI',
    'Proprietary software and its effects on the world',
    'Open source software',
    'Half life 3 and why it will never come out',
    'The darkside of teslas',
    'Discord and its porn problem',
    'Tiktok and misinformation',
    'Rising mental health issues in children',
    'Legalizing marijuana',
    'The fall of object oriented programming',
    'The disfunctional US education system',
    'Parenting in the 21st century',
    'The AI revolution',
    'Potential dangours of modern living',
    'Why you should swap to linux',
    'Reasons to stop using tiktok',
    'Infulencer rug pulls',
    'Big pharma and how they treat their employees',
    'Moist critical and his impact on the gaming industry'
]
newFile = "itzCozi/The-Daily-Compress/data/article.txt"

# Functions
def clear():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Console cleared - AT: ["+datetime.datetime+"]")

    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def getIdea():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Idea fetched - AT: ["+datetime.datetime+"]")

    idea = random.choice(topics)
    topics.remove(idea)
    formattedIdea = "Write an article about " + idea
    return formattedIdea

def write_request(getIdea):
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("API reqeuest made - AT: ["+datetime.datetime+"]")

    # Request AI answer
    response = openai.Completion.create(model="text-davinci-002", prompt=(getIdea), temperature=0.8, max_tokens=375)
    with open(newFile, "w") as file:
        file.write(str(response))

    return response

def filter_response():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Response filtered - AT: ["+datetime.datetime+"]")

    with open("data/article.txt", "w") as f:
        article = f.read()
    
        proofread = openai.Edit.create(
        model="text-davinci-edit-001",
        input= article,
        instruction="Remove any uneccesary words and characters")
    
        f.truncate(0)
        f.write(proofread)

# Main
write_request(getIdea())

# Test this code it should output the topic of the article to .txt file
with open("data/article-topic.txt", "w") as f:
    f.write(idea)

time.sleep(2)
filter_response()
clear()
