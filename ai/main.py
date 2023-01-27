'''
TODO: Make a function that will send the article to openAI's text editor and fix the text then makes
the new text into a variable and then writes it to article file.
TODO: Find a way to remove the topic used after it has been used.
TODO: Add a way to automate the topic making process.
TODO: Make a website in a new github repo called "The-Daily-Compress"
TODO: Add function to clear file then print topics to topics.txt file.
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
start = input("Would you like to start? (y/n): ")
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
