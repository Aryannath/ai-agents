from cli import get_user_message
import anthropic
from agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    client = anthropic.Client(os.getenv("ANTHROPIC_API_KEY"))
    agent = Agent(client, get_user_message)
    agent.run()

if __name__ == "__main__":
    main()

