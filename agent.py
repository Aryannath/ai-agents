import os
import sys
import anthropic 

class Agent:

    def __init__(self, client, get_user_message):
        self.client = client
        self.get_user_message = get_user_message

    def run(self):

        conversation = []
        print("\nChat with Claude (type 'exit' to quit)\n")

        while True:
            user_input = self.get_user_message()
            
            if user_input == 'exit':
                print("\n👋 Exiting chat. Goodbye!")
                break
        

