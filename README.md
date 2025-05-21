# 🧠 Build Your Own Python Coding Agent (With Tool Use!)

Ever wanted to make your own **agent** ? Not just a chatbot, but something that can actually **do** things? How tools like Devin or AI-powered IDEs actually work? What if you could build one, an agent that reads your code, makes changes, and creates new files based on your instructions?

This repo is a tiny, tinkerable playground to explore that idea. I'll walks you through how to build a language model powered agent that can read, write, and modify files in your project folder using only Python and a model like LLaMA 3.

---

## 🧭 What Are We Exploring Here?

You’re not building an app. You’re building an **autonomous coder**. YES AN AUTONOMOUS CODER sounds like a lot right.

One that:

- Understands your request ("Summarize this file" or "Create a new script with X").
- Thinks about what tools it needs.
- Uses those tools to take action like writing to a file or listing code in a directory.

This is less about making a coding agent SAAS product and more about **learning how agents think and act**.

---

## 📦 What You Get

Out of the box, this agent can:

✅ Read files  
✅ Create new files  
✅ List files in a folder  
✅ Append or overwrite existing code  
✅ Use LLaMA 3 via OpenRouter to decide what to do  

All orchestrated through a few small Python scripts.

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone <your-repo-url>
cd <your-folder>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

This uses:

```
openai
python-dotenv
```

### 3. Add your model API key

Create a `.env` file with:

```
MODEL_API_KEY=your-openrouter-api-key
```

You can grab a key at [https://openrouter.ai](https://openrouter.ai).  
I'm using `meta-llama/llama-3.3-8b-instruct:free` because it's free, but you can swap this easily in `main.py`.

---

## 🧪 Try It Out

Run the agent:

```bash
python main.py
```

You’ll see:

```
Chat with LLAMA (type 'exit' or 'ctrl+c' to quit)
```

Now try talking to it:

```
Aryan👽: hey can you read tools.py?

AI 🤖: Sure! Here's a quick summary of tools.py:
- read_file: reads content of a file
- write_file: replaces file content
- list_files: lists files in a directory
...
```

Or:

```
Aryan👽: create a new file called test.py
AI 🤖: Done! Want me to add anything to it?
```

Or even:

```
Aryan👽: append a function to multiply two numbers to test.py
AI 🤖: Appended. Now the file contains both sum and multiply functions.
```

It’s magical and it’s simple.

---

## 🔧 The Tools

Here’s what the agent has in its toolbox:

| Tool         | What it does |
|--------------|--------------|
| `read_file`  | Reads and returns file contents |
| `write_file` | Overwrites a file with new content |
| `append_file`| Adds content to the end of a file |
| `create_file`| Makes a new file |
| `list_files` | Lists all files recursively in a folder |

Each tool is defined in `tools.py`, wrapped in a function + metadata (name, description, expected input). The agent chooses when to use them.

---

## 🧠 How It Works

At its core:

- You talk to it via CLI (`cli.py`)
- It uses a local agent (`agent.py`) to process your prompt
- The agent builds a conversation, decides when to call a tool, and sends all of that to the LLM
- If the LLM wants to call a tool, we do it then feed the result back to the model.
- Continue the conversation.
- Get the desired output.

It’s like giving your LLM a memory and a toolbox to work for you.

---

## 🪜 Example Walkthrough

You might start with:

```
Aryan👽: list all .py files
AI 🤖: ['cli.py', 'agent.py', 'main.py', 'tools.py']
```

Then say:

```
Aryan👽: what's inside agent.py?
AI 🤖: It defines the Agent class, handles tool usage, wraps messages, and communicates with the LLM.
```

Then try:

```
Aryan👽: write a 2 sum function into cc.py
AI 🤖: All set. You can now run cc.py to test the function.
```

You’re not copying and pasting code. You’re describing intent and the agent takes care of the rest.

---

## 📁 Folder Structure

```
.
├── agent.py        # Core agent logic
├── cli.py          # Command-line interface
├── main.py         # Entry point
├── tools.py        # All available tools
├── .env            # API key config
├── requirements.txt
```

---

## ✨ Extend It Yourself

Want to add your own tool? Super simple:

Define a function first for what the tool will do.

```python
new_tool = Tool(
    name="your_tool",
    description="What this tool does and what input it expects.",
    func=your_function
)
```

Then just add it to the `tools` list in `main.py`. Boom — your agent has a new skill.

---

## 🌱 Why This Matters

LLMs are good at *talking*, but they become powerful when they can *act*.

This repo is a seed for building agents that don’t just answer questions but **do things**. Start here. Then scale up. Add memory. Add planning. Add real-world tasks. Build More.

---

## 📬 Reach Out

Curious how this works? Want to jam on agents, dev tools, or new ai trends in general ?

Feel free to fork, experiment, and reach out.

Happy building! 🤖
