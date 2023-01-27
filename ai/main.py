'''
READ NOTES ON DESK FOR MORE INFO
TODO: Add a way to automate the topic making process.
TODO: Implement timer function to activate the writer at a certain time
TODO: Fix date error in logs.log before adding log.html
TODO: Make README.md really fancy (main Branch)
TODO: Add log.html page where the logs.log is displayed in a iframe
'''

# Imports
import os
import random
import time
import datetime
import openai

# Load API key
openai.api_key = "Not for public use"


# Variables
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
newFile = "data/article.txt"


# Functions
def readFile():
  with open("data/article.txt", "w+") as f:
    for line in f:
      f.readline()

def clear():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Console cleared - AT: "+str(datetime.date))

    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def getIdea():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Idea fetched - AT: "+str(datetime.date))

    idea = random.choice(topics)       
    formattedIdea = "Write an article about " + idea
    return formattedIdea

def write_request(getIdea):
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("API reqeuest made - AT: "+str(datetime.date))

    # Request AI answer
    response = openai.Completion.create(model="text-davinci-002", prompt=(getIdea), temperature=0.8, max_tokens=375)
    with open(newFile, "w") as file:
      file.write(str(response))
    return response

def filter_response():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Response filtered - AT: "+str(datetime.date))

    with open("data/article.txt", "w+") as f:
        proofread = openai.Edit.create(
        model="text-davinci-edit-001",
        input= str(readFile()),
        instruction="Fix grammar, spelling and puncation errors")
    
        f.truncate(0)
        f.write(str(proofread))


# Main
write_request(getIdea())
time.sleep(2)
clear()
