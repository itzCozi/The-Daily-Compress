'''
READ NOTES ON DESK FOR MORE INFO
TODO: Add a way to automate the topic making process.
TODO: Implement timer function to activate the writer at a certain time
TODO: Fix date error in logs.log before adding log.html
TODO: Make README.md really fancy (main Branch)
TODO: Make a graph on front README demonstrating refresh process [example](https://github.com/ZeroMemoryEx/U-Boat/edit/master/README.md)
TODO: Add log.html page where the logs.log is displayed in a iframe
'''

# Imports
import os
import time
import openai
from topic_maker import getIdea
from article_writer import write_request

# Variables
idea = getIdea()
topicFile = "/workspaces/Online-Workspace/Workspace/Chat-GPT-API-Article-Writer/src/topics.txt"
newFile = "/workspaces/Online-Workspace/Workspace/Chat-GPT-API-Article-Writer/article.txt"

# Functions
def clear():
    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def readTopics():
    with open(topicFile, "r") as file:
        print(file.read())
        time.sleep(2)

# Main
start = input("Would you like to start? (y/n):")
if start=='y':
    write_request(getIdea())
    print("Article written to article.txt file.")
    time.sleep(2)
    clear()
    
elif start=='n':
    print("Ok, bye!")
    time.sleep(2)
    clear()
    
else:
    print("Invalid input, please try again.")
    time.sleep(2)
    clear()
