# Example 2: Data Transformer

> **Difficulty:** Intermediate | **Time:** ~30 minutes | **Focus:** Iterating on a plan, steering Agent Mode, asking Copilot to explain code

---

## Objective

Practice **refining a plan** and **steering Agent Mode** when the output isn't quite right. You'll deliberately start with a vague prompt, observe how Copilot fills in the gaps (and where it guesses wrong), then iterate to get a better result.

## The Task

Build a Python script that:
- Reads a mock API response from a JSON file (`mock_api_response.json`)
- Transforms the nested data structure into a flat dictionary (`{hostname: ip_address}`)
- Uses that dictionary to create an interactive "Guess the IP" quiz game
- Tracks the player's score and displays it at the end

---

## Step 1: Start with a Deliberately Vague Prompt

Open Copilot Chat and write a **vague** prompt on purpose. The goal is to see how Copilot interprets ambiguity.

### Starting Prompt (Intentionally Vague)

> *"Build a game from the data in `mock_api_response.json`."*

### What to Observe

Look at the plan Copilot produces. Notice:

- **What did Copilot assume?** What kind of game did it decide to build?
- **What's missing?** Did it plan to read from the file? Handle errors? Track a score?
- **What's wrong?** Did it understand the data structure, or is it guessing about the JSON format?
- **What's extra?** Did it add features you didn't ask for?

Write down 2-3 things the plan got wrong or missed. You'll fix these in the next step.

---

## Step 2: Refine the Prompt

Now rewrite your prompt with the missing details. Add the constraints and specifics that were absent from your first attempt.

### Refined Prompt (Example)

> *"Create a Python script called `data_transformer.py` that:*
>
> *1. Reads `mock_api_response.json` (which contains a nested API response with server data)*
> *2. Transforms the data into a flat dictionary where keys are hostnames and values are IP addresses. The JSON structure has servers nested under `data` → each server has `hostname` and `network.ip_address`*
> *3. Creates an interactive quiz game: show the user a hostname, ask them to type the IP address, and tell them if they're correct*
> *4. Tracks the score (correct answers out of total questions)*
> *5. After all servers are asked (or the user types 'quit'), display the final score*
>
> *Requirements:*
> - *Use functions: one for loading/transforming data, one for the game loop*
> - *Use the `json` module (no external packages needed for this)*
> - *Handle the case where the JSON file doesn't exist*
> - *No classes — keep it simple with functions"*

### What Changed

| Original | Refined |
|---|---|
| "build a game" | Specific game type: IP address guessing quiz |
| No data format info | Exact JSON path: `data` → `hostname`, `network.ip_address` |
| No structure requirements | Functions for data loading and game loop |
| No error handling | Handle missing file |
| No exit mechanism | "quit" command to stop early |

---

## Step 3: Execute and Steer

Let Agent Mode implement the refined plan. But this time, **actively steer** during execution:

### While Agent Mode Works

- If it starts creating a class → interrupt: *"Use plain functions, not a class."*
- If it uses `print` for everything instead of formatted output → redirect: *"Format the output more clearly — show the question number, like 'Question 3/8: ...'."*
- If it doesn't handle the 'quit' command → add: *"Also handle when the user types 'quit' to exit early."*

### After Agent Mode Finishes

Ask Copilot to explain anything you don't fully understand:

- *"Explain what the `json.load()` call does and why we use `with open()` instead of just `open()`."*
- *"Why did you use `.get()` instead of direct dictionary access for the network data?"*

This is key — **understanding the code is part of the exercise**, not just getting it to run.

---

## Step 4: Review

### Review Checklist

- [ ] **Data transformation:** Does it correctly extract hostnames and IPs from the nested JSON?
- [ ] **Game loop:** Does it ask a question, get input, check the answer, track score?
- [ ] **Quit handling:** Can the user type "quit" to exit early?
- [ ] **Score display:** Does it show the final score at the end?
- [ ] **Error handling:** What happens if `mock_api_response.json` is missing?
- [ ] **Simplicity:** Is it using functions (not classes)? Is it under ~80 lines?
- [ ] **You understand it:** Can you explain every function?

---

## Step 5: Test It

```bash
python data_transformer.py
```

### Expected Interaction

```
=== Server IP Quiz ===
Type the IP address for each server. Type 'quit' to exit.

Question 1/8: What is the IP address of web-server-01?
Your answer: 192.168.1.10
✅ Correct!

Question 2/8: What is the IP address of db-primary?
Your answer: 10.0.0.50
❌ Wrong! The correct answer is 10.0.0.55.

Question 3/8: What is the IP address of cache-node-01?
Your answer: quit

Final Score: 1/2 (50%)
Thanks for playing!
```

---

## Step 6: Reflect

This exercise taught a different lesson than Example 1:

| Example 1 | Example 2 |
|---|---|
| Clear prompt → good plan → execute | Vague prompt → flawed plan → refine → better plan → execute |
| Focus: writing a good first prompt | Focus: iterating on a plan through feedback |
| Review: is the code correct? | Review: did Copilot understand my intent? |

Ask yourself:
1. **How much did the plan improve** after refining the prompt?
2. **What assumptions did Copilot make** from the vague prompt?
3. **Did you need to steer** Agent Mode during execution? What went wrong?
4. **Did asking Copilot to explain** help you understand the code better?

---

## Copilot Skills Practiced

| Skill | What You Did |
|---|---|
| Recognizing vague prompts | Started with a deliberately vague prompt to see the consequences |
| Iterating on a plan | Refined the prompt with missing constraints and specifics |
| Steering Agent Mode | Interrupted and redirected when the implementation went wrong |
| Asking for explanations | Used Copilot Chat to understand generated code |
| Reviewing for over-engineering | Checked that the solution was appropriately simple |

---

## Reference

### Data File

The `mock_api_response.json` file simulates an API response with this structure:

```json
{
  "status": "success",
  "timestamp": "2026-04-13T10:00:00Z",
  "data": [
    {
      "hostname": "web-server-01",
      "role": "web",
      "datacenter": "us-east-1",
      "network": {
        "ip_address": "192.168.1.10",
        "subnet": "192.168.1.0/24",
        "gateway": "192.168.1.1"
      }
    }
  ]
}
```

See [mock_api_response.json](mock_api_response.json) for the full dataset.

## Success Criteria

- [ ] Script loads and transforms the JSON data correctly
- [ ] Interactive quiz works — asks questions, checks answers
- [ ] User can quit early by typing "quit"
- [ ] Final score is displayed
- [ ] Script handles missing file gracefully
- [ ] Code uses functions (not classes)
- [ ] You refined your prompt at least once before executing
- [ ] You asked Copilot to explain at least one piece of generated code
