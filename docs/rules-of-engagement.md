# Rules of Engagement: Working with GitHub Copilot

> **Copilot is your accelerator, not your replacement. You drive, Copilot assists. Develop gradually, review continuously.**

This guide defines how to collaborate actively with Copilot to get the best results. The goal is to make you faster while keeping you in control — not to make you passive.

---

## The Core Problem

The most common mistake teams make when adopting Copilot is treating it as a **magic box**: write one big prompt, accept everything it generates, ship it, and move on. This leads to:

- Code nobody on the team understands
- Bugs that are harder to find because nobody reviewed the logic
- Over-engineered solutions that are painful to maintain
- A false sense of productivity — you shipped fast, but the code is fragile

The fix is simple: **develop gradually, review continuously**.

---

## ✅ DO — Active, Iterative Collaboration

### 1. Break work into small, reviewable steps
Don't ask Copilot to build an entire application in one prompt. Ask for one function, one module, one feature at a time. Review each piece before moving to the next.

**Instead of:** *"Build a complete REST API client with authentication, retry logic, caching, and CLI interface."*

**Try:** *"Create a function that authenticates against the API and returns a session token."* → review → *"Now add a function that queries the /devices endpoint using that token."* → review → continue.

### 2. Review each piece of generated code before moving on
Read what Copilot produced. Does it make sense? Is it what you asked for? Does it follow your project's patterns? Only proceed to the next step after you're satisfied with the current one.

### 3. Iterate on the plan
After Planning Mode produces a plan, don't just approve it. Read it critically.
- Is anything missing?
- Is it over-scoped?
- Does it match your mental model?

Refine the prompt with constraints: *"Good plan, but simplify step 3 — I don't need a separate config file, just use environment variables."*

### 4. Use Planning Mode before Agent Mode
Always align on the approach before letting Copilot execute. Planning Mode is your opportunity to shape the direction. Skipping it means Copilot guesses — and guesses aren't always right.

### 5. Read and understand generated code
You own every line Copilot writes. If you ship it, you maintain it. If there's a bug at 2 AM, you debug it. Make sure you understand what the code does before it goes into your project.

### 6. Provide context incrementally
Start with the big picture, then drill into specifics. As Copilot builds more of your project, it gains context from the existing code — use that to your advantage.

### 7. Ask Copilot to explain what you don't understand
If Copilot generates code with a pattern you've never seen, don't just accept it. Ask: *"Explain what the `@retry` decorator does in this context."* Copilot is also a teaching tool.

### 8. Test generated code immediately
After each step, run the code. Check it works. Don't accumulate 200 lines of untested code and then discover nothing works.

### 9. Use Copilot Chat to discuss alternatives
Before committing to a design, ask: *"What are the pros and cons of using `argparse` vs `click` for this CLI?"* Let Copilot help you think, not just code.

### 10. Keep your domain knowledge active
Copilot doesn't know your team's conventions, your deployment environment, or your performance requirements. You do. Validate every suggestion against your context.

---

## ❌ DON'T — Passive, All-or-Nothing Anti-Patterns

### 1. Don't write one massive prompt and accept everything
This is the single biggest anti-pattern. A 500-word prompt produces a 500-line output that nobody will review carefully. Break it up.

### 2. Don't skip reading the plan
The plan is your control point. If the plan is wrong, the code will be wrong. Always review and refine before approving execution.

### 3. Don't let Agent Mode run unchecked on large scopes
If you ask Agent Mode to "refactor the entire project," it will — and you'll get a 50-file diff that's impossible to review. Scope your requests narrowly.

### 4. Don't accept code you don't understand
If you can't explain what a function does, you can't debug it, extend it, or maintain it. Ask Copilot to explain it. If the explanation doesn't help, ask for a simpler approach.

### 5. Don't treat Copilot output as "done"
Every piece of generated code is a **first draft**. It needs your review, your context, your judgment. The final version is always a collaboration between you and Copilot.

### 6. Don't blindly trust generated tests
Copilot can write tests that pass but don't actually test anything meaningful. Check that tests cover:
- Real behavior, not just return types
- Edge cases and error paths
- Actual integration with the code, not mocked-out stubs of everything

### 7. Don't use Copilot as a crutch to avoid learning
If Copilot writes a list comprehension and you don't know what a list comprehension is, that's a learning opportunity — not a reason to move on. Use Copilot to learn, not to avoid learning.

### 8. Don't accumulate large diffs before reviewing
The longer you wait to review, the harder it is. Review after each step, not after the entire feature is built. Catching a wrong approach at step 2 is cheap; catching it at step 10 is expensive.

### 9. Don't assume Copilot knows your project conventions
Guide it. Tell it: *"In this project, we use `logging` instead of `print`. All functions have type hints. Error messages start with 'ERROR:'."* Copilot follows conventions when you tell it about them.

### 10. Don't let Copilot over-engineer
If Copilot suggests a factory pattern for a problem that needs an `if` statement, push back: *"This is simpler than that. Just use a dictionary lookup."* You're the architect.

---

## The "Develop Gradually" Workflow

This is the workflow you should practice in every exercise and adopt in your daily work.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   1. PLAN                                               │
│   ┌──────────────────────────────────────────┐          │
│   │  Write a Planning Mode prompt            │          │
│   │  → Copilot produces a plan               │          │
│   │  → You review and refine the plan        │          │
│   └──────────────────────────────────────────┘          │
│                     │                                   │
│                     ▼                                   │
│   2. EXECUTE (one step at a time)                       │
│   ┌──────────────────────────────────────────┐          │
│   │  Approve one step from the plan          │          │
│   │  → Agent Mode implements it              │          │
│   │  → You review the diff                   │          │
│   └──────────────────────────────────────────┘          │
│                     │                                   │
│                     ▼                                   │
│   3. VERIFY                                             │
│   ┌──────────────────────────────────────────┐          │
│   │  Test what was just built                │          │
│   │  → Does it work?                         │          │
│   │  → Does it match the plan?               │          │
│   └──────────────────────────────────────────┘          │
│                     │                                   │
│                     ▼                                   │
│   4. REPEAT                                             │
│   ┌──────────────────────────────────────────┐          │
│   │  Move to the next step                   │          │
│   │  → Each cycle: you understand more       │          │
│   │  → Each cycle: Copilot has more context  │          │
│   └──────────────────────────────────────────┘          │
│                     │                                   │
│                     ▼                                   │
│   5. SHIP                                               │
│   ┌──────────────────────────────────────────┐          │
│   │  Ship incrementally                      │          │
│   │  → Never accumulate massive changesets   │          │
│   │  → Commit after each verified step       │          │
│   └──────────────────────────────────────────┘          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### In Practice

| Step | What You Do | What Copilot Does |
|---|---|---|
| **Plan** | Write a prompt with context, constraints, and goals | Produces a structured plan |
| **Review Plan** | Check for gaps, over-engineering, wrong assumptions | Waits for your feedback |
| **Refine** | Add missing requirements, remove unnecessary steps | Updates the plan |
| **Execute Step 1** | Approve step 1 for implementation | Writes the code |
| **Review Code** | Read the diff, check logic, verify patterns | Waits for your feedback |
| **Test** | Run the code, verify output | — |
| **Execute Step 2** | Approve step 2 | Writes more code, using step 1 as context |
| **...** | Repeat until done | — |
| **Ship** | Commit, push, create PR | — |

---

## Quick Self-Check

Before you accept any Copilot output, ask yourself:

1. **Can I explain this code to a teammate?** If no → ask Copilot to explain it.
2. **Does this match what I asked for?** If no → re-prompt with more specifics.
3. **Is this simpler than my problem requires?** If yes → ask for a more robust version.
4. **Is this more complex than my problem requires?** If yes → ask for simplification.
5. **Have I tested it?** If no → test it now, before moving on.

---

## Summary

| Mindset | Behavior |
|---|---|
| **I'm the architect** | I decide the approach; Copilot implements it |
| **I develop gradually** | One step at a time, reviewed and tested |
| **I stay in control** | I review every change; nothing ships without my understanding |
| **I learn along the way** | I ask Copilot to explain what I don't know |
| **I use Copilot to go faster** | Not to go blindly |
