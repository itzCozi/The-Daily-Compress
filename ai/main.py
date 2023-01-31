# Article-Writer Version.web-BETA-1.0.3
'''
READ NOTES ON DESK FOR MORE INFO
TODO: Add a way to automate the topic making process.
TODO: Make a graph on front README demonstrating refresh process (https://github.com/ZeroMemoryEx/U-Boat/edit/master/README.md)
TODO: Add log.html page where the logs.log is displayed in a iframe
'''

# Imports
import os
import random
import time
import openai
import datetime
from colorama import Fore, Style

# Load API key
openai.api_key = "PRIVATE KEY"


# Variables
debug = True
newFile = "data/article.txt"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

# Load topics into 'data' list
topicFile = open("data/topics.txt", "r")
data = topicFile.read()

data_into_list = data.split("\n")
print(data_into_list)
topicFile.close()


# Functions
def clear():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Console cleared - AT: "+str(date.strftime))
    if debug:
        print("Console cleared - AT: "+str(date.strftime))

    with open("ai/logs.log", "a") as f:
      f.write("Console cleared - AT: "+now)
    if debug==True:
      print(Fore.BLUE+"Console cleared - AT: "+now+Style.RESET_ALL)
  
    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def getIdea():
    # Log
    with open("ai/logs.log", "w") as f:
        f.write("Idea fetched - AT: "+str(date.strftime))
    if debug:
        print()
    with open("ai/logs.log", "a") as f:
        f.write("Idea fetched - AT: "+now)
    if debug==True:
      print(Fore.BLUE+"Idea fetched - AT: "+now+Style.RESET_ALL)

    idea = random.choice(data_into_list)
    formattedIdea = "Write an article about " + idea
    clear() 

    # Read the contents of the file into a list
    with open("data/topics.txt", "r") as f:
      DELtopics = f.read().splitlines()

    # Remove the topic
    DELtopics.remove(idea)

    # Write the updated list back to the file
    with open("data/topics.txt", "w") as f:
      f.write('\n'.join(DELtopics))
      print("TOPIC DELETED")
  
    print("Prompt: "+formattedIdea)
    print("Topic: "+idea)
    return formattedIdea

def readFile():
  with open("data/article.txt", "w+") as f:
    for line in f:
      f.readline()

def write_request(getIdea):
    # Log
    with open("ai/logs.log", "a") as f:
      f.write("API reqeuest made - AT: "+now)
    if debug==True:
      print(Fore.BLUE+"API reqeuest made - AT: "+now+Style.RESET_ALL)

    # Request AI answer
    response = openai.Completion.create(
      model="text-davinci-002", 
      prompt=(getIdea), 
      temperature=0.8, 
      max_tokens=400)
    
    with open(newFile, "w") as file:
      file.write(str(response))
    return response

def filter_response():
    # Log
    with open("ai/logs.log", "a") as f:
      f.write("Response filtered - AT: "+now)
    if debug==True:
      print(Fore.BLUE+"Response filtered - AT: "+now+Style.RESET_ALL)

    with open("data/article.txt", "w+") as f:
        proofread = openai.Edit.create(
        model="text-davinci-edit-001",
        input= str(readFile()),
        instruction="Remove unnecessary characters")
    
        f.truncate(0)
        f.write(str(proofread))


# Main
write_request(getIdea())
time.sleep(2)
clear()
