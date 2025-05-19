from cli import get_user_message
from openai import OpenAI
from agent import Agent
from dotenv import load_dotenv
import os
from tools import read_file_tool,create_file_tool,list_files_tool,append_file_tool,write_file_tool


load_dotenv()

def main():
    client = OpenAI(
        api_key=os.getenv("MODEL_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    
    tools = [read_file_tool,create_file_tool,list_files_tool,append_file_tool,write_file_tool]

    agent = Agent(client, get_user_message, tools)
    agent.run()

if __name__ == "__main__":
    main()

