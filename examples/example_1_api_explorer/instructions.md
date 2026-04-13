# Example 1: API Explorer

> **Difficulty:** Beginner | **Time:** ~30 minutes | **Focus:** Writing your first Planning Mode prompt, executing with Agent Mode

---

## Objective

Use Copilot's **Planning Mode** to design a Python script that fetches data from a public REST API, then use **Agent Mode** to implement it. This is your first practice of the full **Plan → Execute → Review** cycle.

## The Task

Build a Python script that:
- Calls the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts) to fetch a list of blog posts
- Displays the total number of posts
- Prints the title and body preview (first 80 characters) of the first 5 posts
- Handles the case where the API is unreachable

This is intentionally simple — the goal is to practice the **workflow**, not to write complex code.

---

## Step 1: Write a Planning Mode Prompt

Open Copilot Chat in VS Code. Write a prompt describing what you want to build. Don't start coding — start **planning**.

### Suggested Starting Prompt

> *"Create a Python script called `api_explorer.py` that fetches blog posts from `https://jsonplaceholder.typicode.com/posts`. The script should:*
> - *Use the `requests` library to make the API call*
> - *Print the total number of posts found*
> - *Display the title and first 80 characters of the body for the first 5 posts*
> - *Handle errors if the API is unreachable or returns a non-200 status code*
> - *Use functions, not just top-level code*
> - *Include a `if __name__ == '__main__'` block"*

### Tips for Your Prompt

- Be specific about the **output format** — what should the user see when they run the script?
- Mention the **library** you want to use (don't let Copilot choose)
- State **error handling** expectations explicitly
- Reference the **file name** so Copilot knows where to put the code

### What to Look For in the Plan

When Copilot responds with a plan, check:

- [ ] Does it mention using `requests`?
- [ ] Does it plan to create a function for fetching posts?
- [ ] Does it plan error handling for network issues?
- [ ] Does it plan to format the output as described?
- [ ] Is there anything unnecessary? (e.g., creating a class, adding logging, writing tests — you didn't ask for these)

If something is missing or wrong, **refine your prompt** before proceeding. For example:
- *"You forgot to handle the case where the API returns an empty list."*
- *"I don't need a class — just use a plain function."*

---

## Step 2: Execute with Agent Mode

Once you're happy with the plan, let Copilot implement it. Switch to Agent Mode and approve the plan.

While Copilot works, watch what it does:
- What files does it create?
- Does the code match the plan?
- Is it doing anything you didn't ask for?

---

## Step 3: Review the Output

After Agent Mode finishes, review the generated code using this checklist:

### Review Checklist

- [ ] **Correctness:** Does the code call the right URL?
- [ ] **Functions:** Is the logic organized into functions (not all in the global scope)?
- [ ] **Error handling:** What happens if the API is down? Does it crash or show a message?
- [ ] **Output format:** Does it print the title and body preview as described?
- [ ] **Simplicity:** Is the code straightforward, or did Copilot over-engineer it?
- [ ] **No extras:** Did Copilot add features you didn't ask for? (If so, consider asking to remove them)

---

## Step 4: Test It

Run the script:

```bash
pip install requests  # if not already installed
python api_explorer.py
```

### Expected Output (approximately)

```
Found 100 posts.

Post 1: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
  Preview: quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nrepr...

Post 2: qui est esse
  Preview: est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea d...

Post 3: ea molestias quasi exercitationem repellat qui ipsa sit aut
  Preview: et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvolup...

Post 4: eum et est occaecati
  Preview: ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda p...

Post 5: nesciunt quas odio
  Preview: repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\n...
```

### Test Error Handling

Try changing the URL to something invalid and re-run — does it fail gracefully?

---

## Step 5: Reflect

Ask yourself:

1. **Was the plan accurate?** Did the code match what the plan described?
2. **Did you need to refine?** If so, what was missing from your original prompt?
3. **Did Copilot add anything unexpected?** Was it useful or unnecessary?
4. **Could you explain the generated code** to a teammate?

---

## Copilot Skills Practiced

| Skill | What You Did |
|---|---|
| Writing a planning prompt | Described the task with context, constraints, and desired outcome |
| Reviewing a plan | Checked the plan for completeness and accuracy before approving |
| Using Agent Mode | Let Copilot implement the approved plan |
| Reviewing generated code | Checked correctness, simplicity, and error handling |
| Testing immediately | Ran the code right after generation to verify it works |

---

## Reference

### API Details

- **URL:** `https://jsonplaceholder.typicode.com/posts`
- **Method:** GET
- **Authentication:** None required
- **Response:** JSON array of 100 post objects

Each post object looks like:
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

See [sample_data.json](sample_data.json) for a full example response.

## Success Criteria

- [ ] Script runs without errors
- [ ] Displays the total post count
- [ ] Shows title and body preview for 5 posts
- [ ] Handles API errors gracefully (doesn't crash)
- [ ] Code is organized in functions
- [ ] You can explain every line of the generated code
