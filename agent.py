import os
import sys
import anthropic 

class Agent:

    def __init__(self, client, get_user_message):
        self.client = client
        self.get_user_message = get_user_message

        

