import json
import os

class Tool:
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func  # function(input_json: str) -> str

def read_file(input_json: str):
    try:
        data = json.loads(input_json)
        path = data.get("path")
        if not path:
            return "Error: 'path' key is required."
        if not os.path.isfile(path):
            return f"Error: File '{path}' not found."
        with open(path, "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

read_file_tool = Tool(
    name="read_file",
    description="Reads the content of a given file path. Input: JSON with {'path': '<relative path>'}. Output: file content as string.",
    func=read_file,
)



    