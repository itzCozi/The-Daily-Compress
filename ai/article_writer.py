# Imports
import os
import openai
from topic_maker import getIdea

# Load API key
openai.api_key = "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"
 
# Variables
idea = getIdea()
newFile = "itzCozi/The-Daily-Compress/data/article.txt"

# Functions
def clear():
    clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    return clr

def write_request(getIdea):
    # Request AI answer
    response = openai.Completion.create(model="text-davinci-002", prompt=(getIdea), temperature=0.8, max_tokens=375)
    with open(newFile, "w") as file:
        file.write(str(response))

    return response
