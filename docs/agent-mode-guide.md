# Agent Mode Guide

> **Agent Mode lets Copilot execute autonomously — reading files, writing code, running commands. Your job is to review its work like a pull request from a junior developer.**

---

## What Is Agent Mode?

Agent Mode is Copilot working autonomously to implement a task. Unlike inline completions (which suggest the next line), Agent Mode can:

- **Read existing files** to understand your project
- **Create and edit files** across your codebase
- **Run terminal commands** (install packages, run tests, check syntax)
- **Make multi-step changes** that span multiple files

Think of it as a junior developer working from your instructions. The work is usually good, but it needs your review before it's ready to ship.

---

## When to Use Agent Mode

| Good For | Not Good For |
|---|---|
| Implementing a plan you've already reviewed | Exploring a problem you don't understand yet (use Planning Mode first) |
| Writing boilerplate code (CLI setup, logging config) | Making changes to production systems without review |
| Creating tests for existing code | Large-scale refactors without clear scope |
| Building a new feature from a clear spec | Code in languages or frameworks you're unfamiliar with |
| Filling in repetitive patterns | Security-sensitive operations (auth, crypto, permissions) |

---

## The Review Mindset

### Treat It Like a Pull Request

When a junior developer sends you a PR, you don't just click "Approve." You:

1. **Read the description** — does it match what was asked?
2. **Review the diff** — is the code correct, readable, and minimal?
3. **Check for surprises** — any files changed that shouldn't be?
4. **Verify tests** — do they test real scenarios?
5. **Look for anti-patterns** — hardcoded values, missing error handling, over-engineering?

Apply the same discipline to Agent Mode output.

### The Review Checklist

Use this checklist every time Agent Mode produces output:

#### Correctness
- [ ] Does the code do what was asked?
- [ ] Does it follow the approved plan?
- [ ] Are there logic errors or off-by-one mistakes?

#### Scope
- [ ] Were only the intended files modified?
- [ ] Are there any unnecessary changes? (reformatting, reorganizing, extra features)
- [ ] Did it add more than what was requested?

#### Code Quality
- [ ] Is the code readable and well-structured?
- [ ] Can you explain every function to a teammate?
- [ ] Does it follow your project's existing patterns?
- [ ] Are variable and function names clear?

#### Error Handling
- [ ] Are errors handled appropriately? (not too much, not too little)
- [ ] Are error messages helpful for debugging?
- [ ] Does it fail gracefully on unexpected input?

#### Security
- [ ] No hardcoded secrets, tokens, or passwords?
- [ ] No unsafe handling of user input?
- [ ] No unnecessary file permissions or network access?

#### Tests (if applicable)
- [ ] Do tests cover actual behavior, not just happy paths?
- [ ] Are edge cases tested? (empty input, network errors, auth failures)
- [ ] Are tests meaningful? (not just `assert True`)

---

## How to Steer Agent Mode

Agent Mode isn't fire-and-forget. You can — and should — steer it during execution.

### Interrupt and Redirect

If you see Agent Mode going in the wrong direction:

1. **Stop it** — click the stop button or press the keyboard shortcut
2. **Explain what's wrong** — *"You're creating a class hierarchy, but I just need plain functions."*
3. **Be specific about the fix** — *"Remove the `BaseClient` class. Make `fetch_devices` a standalone function that takes `url` and `token` as arguments."*

### Add Context Mid-Execution

As Agent Mode works, it may lack context about your preferences:

- *"In this project, we use `logging` instead of `print()` for all output."*
- *"The API returns paginated results. You need to handle the `next` URL in the response."*
- *"We prefix all error messages with the function name, like `[fetch_devices] Error: ...`"*

### Request Changes After Completion

After Agent Mode finishes, you can request modifications:

- *"Good, but add `--verbose` flag support. When set, use `logging.DEBUG` level."*
- *"Simplify the error handling — just catch `RequestException` instead of individual exception types."*
- *"Add type hints to all function signatures."*

---

## Common Agent Mode Mistakes (and How to Fix Them)

### 1. Over-Engineering

**Symptom:** Copilot creates abstract base classes, factory methods, or design patterns for a simple script.

**Fix:** *"This is a simple single-file script. Remove the class hierarchy and use plain functions. No need for abstraction — this won't be extended."*

### 2. Modifying Unrelated Files

**Symptom:** Agent Mode "helps" by reformatting or updating files you didn't ask about.

**Fix:** *"Revert changes to `config.py` and `utils.py`. Only modify `query.py` as requested."*

### 3. Superficial Tests

**Symptom:** Tests only check that functions don't throw errors, without verifying behavior.

```python
# Bad test — passes but tests nothing
def test_fetch_devices():
    result = fetch_devices("http://example.com", "token")
    assert result is not None  # This tells us nothing
```

**Fix:** *"These tests don't verify behavior. Rewrite to check: (1) correct devices are returned for valid input, (2) empty list for no matches, (3) RuntimeError is raised for 401 responses."*

### 4. Ignoring Project Conventions

**Symptom:** Copilot uses `print()` when your project uses `logging`, or adds type annotations your project doesn't use.

**Fix:** Provide conventions upfront: *"Follow these conventions: use `logging` for output, snake_case for functions, no type hints, docstrings for all public functions."*

### 5. Hallucinated APIs or Arguments

**Symptom:** Copilot uses API endpoints or function arguments that don't exist.

**Fix:** Always verify API calls against actual documentation. Provide the API docs or example responses in your prompt.

---

## Working with Agent Mode Effectively

### The Incremental Approach

Don't ask Agent Mode to build everything at once. Use it in small, verifiable steps:

```
Step 1: "Create the argument parser with search_term, --url, and --token arguments."
  → Review → Test: python tool.py --help
  
Step 2: "Add the API query function. Accept url and token. Return the JSON response."
  → Review → Test: Add a quick print(query(...)) call
  
Step 3: "Add error handling for network errors and auth failures."
  → Review → Test: Try with a wrong URL, wrong token
  
Step 4: "Add logging. Replace print() with logging.info(). Add --verbose flag."
  → Review → Test: Run with and without --verbose
```

Each step builds on the previous one. Each step is small enough to review thoroughly.

### Providing Good Context

Agent Mode works best when it has context. Help it by:

- **Opening relevant files** in your editor before starting
- **Mentioning file paths** in your prompt: *"Update the `query_devices` function in `src/client.py`."*
- **Referencing existing patterns**: *"Follow the same pattern used in `fetch_users()` for error handling."*
- **Sharing example data**: *"The API response looks like this: `{"results": [{"name": "device-1", "primary_ip": {"address": "10.0.0.1/24"}}]}`"*

### Knowing When to Take Over

Sometimes it's faster to write the code yourself. Agent Mode adds overhead for:

- One-line changes
- Simple renames or moves
- Fixes where you know exactly what to change
- Cases where explaining the fix takes longer than doing it

Use Agent Mode for the parts Copilot is good at (boilerplate, patterns, repetition) and take over for the parts that need your judgment.

---

## Summary

| Principle | Action |
|---|---|
| **Review everything** | Treat Agent Mode output like a PR — never auto-accept |
| **Scope narrowly** | One feature, one function, one step at a time |
| **Steer actively** | Interrupt, redirect, add context as needed |
| **Verify tests** | Check that tests test real behavior, not just existence |
| **Watch for over-engineering** | Push back on unnecessary complexity |
| **Know when to take over** | Write simple changes yourself — use Agent Mode for the heavy lifting |
