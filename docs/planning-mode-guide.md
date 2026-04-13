# Planning Mode Guide

> **Planning Mode is how you tell Copilot what to build before any code is written. The clearer your plan, the better the result.**

---

## What Is Planning Mode?

Planning Mode is a way of working with Copilot where you ask it to **think through the approach first** — producing a structured, step-by-step plan — before writing any code. You can then review, refine, and approve the plan before letting Copilot execute it.

Think of it as writing a brief for a contractor. You wouldn't tell a builder "make me a house" and walk away. You'd discuss the layout, materials, requirements, and budget first. Planning Mode is that discussion.

### When to Use It

- **Starting a new script or feature** — align on the approach before coding
- **Tackling an unfamiliar problem** — let Copilot help you think through the steps
- **Complex tasks with multiple parts** — break them into a clear sequence
- **When you want to compare approaches** — ask Copilot for alternatives before committing

### When NOT to Use It

- Quick one-liners (just type and accept the inline suggestion)
- Fixing a typo or renaming a variable
- When you already know exactly what to write and just want completion speed

---

## Anatomy of a Good Planning Prompt

A good planning prompt has three parts: **Context**, **Constraints**, and **Desired Outcome**.

### The Three Parts

```
┌─────────────────────────────────────────────┐
│  1. CONTEXT         What exists already?    │
│  2. CONSTRAINTS     What are the rules?     │
│  3. DESIRED OUTCOME What should it do?      │
└─────────────────────────────────────────────┘
```

### Part 1: Context — What exists already?

Tell Copilot what it's working with. Reference existing files, libraries, patterns, or conventions.

**Examples:**
- *"I have a Python project that uses `requests` for API calls and `argparse` for CLI arguments."*
- *"The project structure has a `src/` folder with `client.py` and `models.py`."*
- *"We use `logging` for all output — no `print()` statements."*

### Part 2: Constraints — What are the rules?

Define boundaries so Copilot doesn't over-engineer or choose the wrong tools.

**Examples:**
- *"Use only the standard library plus `requests`. No other external packages."*
- *"The script should be a single file, under 150 lines."*
- *"Don't create a class — use plain functions."*
- *"Error messages should use `logging.error()`, not `print()`."*

### Part 3: Desired Outcome — What should the end result look like?

Describe the behavior, not just the code structure. What should the script do? What should the user experience be?

**Examples:**
- *"The tool should accept a search term as a positional argument and print matching results in a table."*
- *"If the API returns an error, the tool should log the error and exit with code 1."*
- *"Running `python tool.py --help` should show usage with all available options."*

---

## Effective vs. Ineffective Prompts

### ❌ Too Vague

> *"Build me an API client."*

**What's wrong:** No context about which API, what language, what the client should do, or what format the output should be in. Copilot will guess everything.

### ❌ Too Narrow

> *"Write a for loop that iterates over the list and prints each item."*

**What's wrong:** This doesn't need Planning Mode — it's a single line of code. Use inline completion instead.

### ❌ Missing Context

> *"Add error handling."*

**What's wrong:** To what? For which errors? What should happen when an error occurs? Copilot can't read your mind about project conventions.

### ✅ Good — Simple Task

> *"Create a Python function called `fetch_posts` that calls `https://jsonplaceholder.typicode.com/posts`, returns the JSON response as a list of dicts, and raises a `RuntimeError` if the status code isn't 200. Use the `requests` library."*

**Why it works:** Clear function name, specific API, defined return type, explicit error behavior, named library.

### ✅ Good — Complex Task

> *"Create a Python CLI tool for querying a device inventory API. Requirements:*
> - *Use `argparse` with a required `search_term` positional argument and optional `--url` and `--token` flags*
> - *Get the API token from the `--token` argument if provided, otherwise from the `INVENTORY_API_TOKEN` environment variable*
> - *Use `logging` (not `print`). Default level: INFO. Add a `--verbose` flag for DEBUG level*
> - *Handle network errors with `try/except requests.exceptions.RequestException`*
> - *Print results as: `{device_name} — {ip_address}`*
> - *Single file, use `if __name__ == '__main__'` pattern"*

**Why it works:** Specific requirements for every aspect — CLI design, authentication, logging, error handling, output format, and code structure. Copilot has almost no room to guess wrong.

---

## How to Iterate on a Plan

Your first prompt rarely produces a perfect plan. That's expected. The iteration is where the value is.

### Step 1: Review the Initial Plan

After Copilot produces a plan, read it and ask:
- Does the plan cover all my requirements?
- Is anything missing? (edge cases, error handling, tests)
- Is anything unnecessary? (features I didn't ask for, abstractions I don't need)
- Does the ordering make sense?

### Step 2: Refine with Targeted Feedback

Don't rewrite the entire prompt. Give incremental feedback:

- **Add a missing step:** *"The plan is missing error handling for 401 responses. Add a step to check for auth errors and log a specific message."*
- **Remove unnecessary complexity:** *"Step 4 creates a separate config class — that's overkill. Just read from environment variables directly."*
- **Reorder steps:** *"Move the logging setup before the API call so we can log the URL we're about to query."*
- **Change approach:** *"Instead of writing all results to a file, just print them to stdout and let the user redirect if they want."*

### Step 3: Ask for Alternatives

If the plan doesn't feel right, ask Copilot for a different approach:

- *"Can you suggest an alternative approach that doesn't require a class?"*
- *"What would this look like with `click` instead of `argparse`?"*
- *"Show me a simpler version that handles just the happy path first."*

### Step 4: Approve and Execute

Once the plan matches your expectations, tell Copilot to proceed. This transitions to Agent Mode where Copilot implements the plan.

---

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| **Prompt is a novel** — 500 words describing every edge case | Break it into smaller prompts. Plan one feature at a time. |
| **No constraints** — Copilot picks its own tools and patterns | Always state: language, libraries, output format, code structure. |
| **Approving without reading** — the plan looks "long enough" | Read every step. A wrong plan produces wrong code. |
| **Never iterating** — accepting the first plan always | The first plan is a draft. Refine at least once. |
| **Forgetting context** — not mentioning existing code or conventions | Reference existing files and patterns. Copilot can't see what you don't mention. |

---

## Prompt Templates

Use these as starting points and customize for your task.

### Template: New Script

> *"Create a Python script that [WHAT IT DOES]. It should:*
> - *[REQUIREMENT 1]*
> - *[REQUIREMENT 2]*
> - *[REQUIREMENT 3]*
>
> *Constraints: [LIBRARIES/PATTERNS/LIMITS]*
>
> *Expected usage: `python script.py [ARGS]`"*

### Template: Add a Feature

> *"Add [FEATURE] to the existing [FILE/MODULE]. Currently, it [WHAT IT DOES NOW]. After this change, it should also [NEW BEHAVIOR].*
>
> *Keep the existing API unchanged. Use [LIBRARY/PATTERN] for the new functionality."*

### Template: Refactor

> *"Refactor [FUNCTION/MODULE] to [GOAL — e.g., improve testability, reduce duplication, extract a reusable component]. The current code [DESCRIPTION OF CURRENT STATE]. The refactored version should [DESIRED STATE].*
>
> *Don't change the external interface — only internal implementation."*

---

## Summary

1. **Always start with Planning Mode** for non-trivial tasks
2. **Write prompts with Context + Constraints + Desired Outcome**
3. **Review the plan** — don't approve blindly
4. **Iterate at least once** — refine, remove, reorder
5. **Then execute** — move to Agent Mode with a plan you trust
