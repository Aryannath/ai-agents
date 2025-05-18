import os
import sys
from typing import List
import json
from tools import Tool,read_file
import ast

class Agent:

    def __init__(self, client, get_user_message,tools):
        self.client = client
        self.get_user_message = get_user_message
        self.conversation = []
        self.tools = tools

    def run(self):

        print("\nChat with GEMINI (type 'exit' or 'ctrl+c' to quit)\n")
        
        try:
            while True:
                user_input = self.get_user_message()
                
                if user_input == 'exit':
                    print("\n👋 Exiting chat. Goodbye!")
                    break
                
                self.conversation.append({"role": "user", "content": user_input})

                message = self.run_inference(self.conversation)

                if not message:
                    print("Error getting response.")
                    return

                try:
                    parsed = ast.literal_eval(message)
                except Exception:
                    parsed = {}

                if isinstance(parsed, dict) and "tool_use" in parsed:

                    tool_name = parsed["tool_use"]["name"]
                    tool_input = json.dumps(parsed["tool_use"]["input"])  # input as json string
                    tool = next((t for t in self.tools if t.name == tool_name), None)

                    if tool:
                        tool_result = tool.func(tool_input)
                    else:
                        tool_result = f"Error: Tool '{tool_name}' not found."

                    # Append tool result as user message and ask model again
                    self.conversation.append({"role": "assistant", "content": message})
                    self.conversation.append({"role": "user", "content": tool_result})

                    # Run inference again to get final reply
                    response = self.run_inference(self.conversation)

                    print(f"\nAI 🤖: {response}\n")
                    self.conversation.append({"role": "assistant", "content": response})
                    print("\n" + "-"*60 + "\n")

                else:
                    print(f"\nAI 🤖: {message}\n")
                    print("\n" + "-"*60 + "\n")
                
                self.conversation.append({"role": "assistant", "content": message})

        except KeyboardInterrupt:
            print("\n👋Goodbye!")
    
    def run_inference(self, conversation):
        try:
            tool_descriptions = "\n".join(
                [f"Tool: {t.name} - {t.description}" for t in self.tools]
            )
            system_prompt = f"You have access to the following tools:\n{tool_descriptions}\nIf you want to use a tool, only respond the dictionary not reasoning, respond in the format:\n{{'tool_use': {{'name': <tool_name>, 'input': <json_string>}}}}\nOtherwise, respond normally."

            conversation = [{"role": "system", "content": system_prompt}] + conversation

            response = self.client.chat.completions.create(
                model="meta-llama/llama-3.3-8b-instruct:free",
                messages=conversation,
                max_tokens=1024,
                temperature=0.7
            )
            # print(conversation)
            # print(response)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during inference: {e}")
            return None
        

