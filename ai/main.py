'''
TODO: Make a function that will send the article to openAI's text editor and fix the text then makes
the new text into a variable and then writes it to article file.
TODO: Maybe add a simple parser to completly automate the process.
TODO: Add a way to automate the topic making process.
TODO: Add function to clear file then print topics to topics.txt file.
TODO: Add footer to article with anchor links to about page and other pages.
'''

# Imports
import os
import random
import time
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
    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def getIdea():
    idea = random.choice(topics)
    topics.remove(idea)
    formattedIdea = "Write an article about " + idea
    return formattedIdea

def write_request(getIdea):
    # Request AI answer
    response = openai.Completion.create(model="text-davinci-002", prompt=(getIdea), temperature=0.8, max_tokens=375)
    with open(newFile, "w") as file:
        file.write(str(response))

    return response


# Main
write_request(getIdea())
time.sleep(2)
clear()
