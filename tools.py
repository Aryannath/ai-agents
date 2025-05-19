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
    func=read_file
)


def create_file(input_json: str):
    try:
        data = json.loads(input_json)
        path = data.get("path")
        content = data.get("content", "")
        if not path:
            return "Error: 'path' key is required."
        # Prevent overwriting existing files accidentally
        if os.path.exists(path):
            return f"Error: File '{path}' already exists."
        with open(path, "w") as f:
            f.write(content)
        return f"File '{path}' created successfully."
    except Exception as e:
        return f"Error creating file: {str(e)}"

create_file_tool = Tool(
    name="create_file",
    description="Creates a new file with given path and content. Input: JSON with {'path': '<relative path>', 'content': '<file content>'}. Output: Success or error message.",
    func=create_file
)

def list_files(input_json: str):
    try:
        data = json.loads(input_json)
        directory = data.get("directory", ".")  # default current dir
        if not os.path.isdir(directory):
            return f"Error: Directory '{directory}' not found."
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.relpath(os.path.join(root, filename), directory))
        return json.dumps(files)  # Return JSON list of files relative to directory
    except Exception as e:
        return f"Error listing files: {str(e)}"

list_files_tool = Tool(
    name="list_files",
    description="Lists all files under the given directory recursively. Input: JSON with {'directory': '<path>'} (optional, default '.'). Output: JSON list of file paths.",
    func=list_files
)


def append_file(input_json: str):
    try:
        data = json.loads(input_json)
        path = data.get("path")
        content = data.get("content", "")
        if not path:
            return "Error: 'path' key is required."
        if not os.path.isfile(path):
            return f"Error: File '{path}' not found."
        with open(path, "a") as f:
            f.write(content)
        return f"Content appended to '{path}' successfully."
    except Exception as e:
        return f"Error appending to file: {str(e)}"

append_file_tool = Tool(
    name="append_file",
    description="Appends content to an existing file. Input: JSON with {'path': '<file_path>', 'content': '<text to append>'}. Output: Success or error message.",
    func=append_file
)


def write_file(input_json: str):
    try:
        data = json.loads(input_json)
        path = data.get("path")
        content = data.get("content", "")
        if not path:
            return "Error: 'path' key is required."
        with open(path, "w") as f:
            f.write(content)
        return f"File '{path}' written successfully."
    except Exception as e:
        return f"Error writing file: {str(e)}"

write_file_tool = Tool(
    name="write_file",
    description="Writes (replaces) content of a file. Input: JSON with {'path': '<file_path>', 'content': '<new content>'}. Output: Success or error message.",
    func=write_file
)
