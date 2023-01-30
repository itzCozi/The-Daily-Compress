'''
READ NOTES ON DESK FOR MORE INFO
TODO: Add a way to automate the topic making process.
TODO: Fix date error in logs.log before adding log.html (https://www.programiz.com/python-programming/datetime/current-datetime)
TODO: Make a graph on front README demonstrating refresh process (https://github.com/ZeroMemoryEx/U-Boat/edit/master/README.md)
TODO: Add log.html page where the logs.log is displayed in a iframe
'''

# Imports
import os
import random
import time
import openai
from datetime import date

# Load API key
openai.api_key = "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"


# Variables
newFile = "data/article.txt"

# Load topics into 'data' list
topicFile = open("data/topics.txt", "r")
data = topicFile.read()

# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
topicFile.close()


# Functions
def clear():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Console cleared - AT: "+str(date.today))

    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def getIdea():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Idea fetched - AT: "+str(date.today))

    idea = random.choice(data_into_list)
    formattedIdea = "Write an article about " + idea
    clear()
    print(formattedIdea)
    return formattedIdea

def readFile():
  with open("data/article.txt", "w+") as f:
    for line in f:
      f.readline()

def write_request(getIdea):
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("API reqeuest made - AT: "+str(date.today))

    # Request AI answer
    response = openai.Completion.create(model="text-davinci-002", prompt=(getIdea), temperature=0.8, max_tokens=375)
    with open(newFile, "w") as file:
      file.write(str(response))
    return response

def filter_response():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Response filtered - AT: "+str(date.today))

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
