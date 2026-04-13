# Getting Started with GitHub Copilot

> **A simple guide for your first day with Copilot. No jargon, no overwhelm — just the basics.**

---

## What Is Copilot?

Copilot is an AI assistant built into VS Code that helps you write code. You talk to it in plain English, and it writes code for you. You review what it wrote, keep the good parts, and fix or redo the rest.

That's it. It's not magic. It's a very fast helper that needs your guidance.

---

## Setup (5 minutes)

1. Open **VS Code**
2. Install the **GitHub Copilot** extension (search "GitHub Copilot" in the Extensions panel)
3. Install the **GitHub Copilot Chat** extension
4. Sign in with your GitHub account (you need a Copilot subscription)
5. You're ready

### Quick Test

Open Copilot Chat (click the chat icon in the sidebar or press `Ctrl+Shift+I` / `Cmd+Shift+I`) and type:

> *"Write a Python function that adds two numbers."*

If Copilot responds with code, you're all set.

---

## The Three Things You Need to Know

### 1. Talk to Copilot Like a Colleague

Don't type code. Type what you **want** in plain words.

**You say:**
> *"Create a Python script that reads a list of names from a file called names.txt and prints each name in uppercase."*

**Copilot gives you:** A working Python script.

The clearer you are about what you want, the better the result.

### 2. Always Review What Copilot Writes

Copilot is fast, but it's not always right. **Read the code before you accept it.** Ask yourself:

- Does this look correct?
- Do I understand what it does?
- Is it what I asked for?

If you don't understand something, ask Copilot: *"Explain this code to me."*

### 3. Work in Small Steps

Don't ask for an entire application at once. Ask for **one thing at a time**:

1. *"Create a function that reads a file."* → review → looks good
2. *"Now add a function that filters the data."* → review → looks good
3. *"Now add error handling for when the file doesn't exist."* → review → done

Small steps = easier to review = fewer mistakes = better code.

---

## Your First Exercise (10 minutes)

Let's try it. Open Copilot Chat and type this:

> *"Create a Python script called hello.py that asks the user for their name, then prints 'Hello, [name]! Welcome to Copilot.' Make it a function called greet_user."*

**After Copilot responds:**

1. Read the code. Does it make sense?
2. Save it as `hello.py`
3. Run it: `python hello.py`
4. Does it work? Great!

**Now try adding to it:**

> *"Update hello.py to also ask for the user's favorite color and include it in the greeting."*

Review the change. Run it again. You just used the **ask → review → build on it** workflow.

---

## The Two Ways to Use Copilot

### Copilot Chat (Recommended for Beginners)

This is the sidebar where you type messages. Use it when:
- You want to **describe** what to build
- You want code **explained**
- You want to **plan** before coding
- You want to **fix** something that's not working

### Inline Suggestions

As you type code, Copilot suggests the next line in gray text. Press `Tab` to accept. Use it when:
- You're already writing code and want it to finish your thought
- You see a suggestion that looks correct

Start with **Chat**. It's more forgiving and gives you time to think.

---

## Common Questions

**Q: What if Copilot gives me wrong code?**
Tell it: *"That's not right. I wanted [what you actually wanted]."* It will try again. You can also just type a better description.

**Q: What if I don't understand the code it wrote?**
Ask: *"Explain this code line by line."* Copilot will walk you through it.

**Q: Can Copilot break my project?**
Only if you accept code without reviewing it. Always read what it writes before saving. If something goes wrong, press `Ctrl+Z` / `Cmd+Z` to undo.

**Q: Is there a wrong way to use it?**
The main mistake is accepting everything without reading it. Take a moment to understand what Copilot wrote — it's faster to fix a small issue now than a big one later.

**Q: How do I get better at this?**
Practice. The more you use Copilot, the better you get at telling it what you want. Start with small tasks and work up.

---

## Cheat Sheet

| What You Want | What to Say |
|---|---|
| Create something new | *"Create a Python script that..."* |
| Explain code | *"Explain this code to me."* |
| Fix a bug | *"This script gives me [error]. Fix it."* |
| Add a feature | *"Add [feature] to this script."* |
| Simplify code | *"Make this code simpler."* |
| Write a test | *"Write a test for this function."* |
| Learn something | *"How does [concept] work in Python?"* |

---

## What's Next?

Once you're comfortable with the basics above, explore the rest of this workshop:

1. **[Rules of Engagement](rules-of-engagement.md)** — Simple do's and don'ts for working with Copilot
2. **[Example 1: API Explorer](../examples/example_1_api_explorer/instructions.md)** — Your first guided exercise
3. **[Planning Mode Guide](planning-mode-guide.md)** — How to ask Copilot to plan before coding (the key to bigger tasks)

Take it at your own pace. There's no rush.
