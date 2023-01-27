# A script that generates a topic for the article writer

# Imports
import time
import openai
import random

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

# Functions
def getIdea():
    idea = random.choice(topics)
    topics.remove(idea)
    formattedIdea = "Write an article about " + idea
    return formattedIdea
