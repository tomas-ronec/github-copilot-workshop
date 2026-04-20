> “This is not a tutorial. It’s a repeatable workshop system for teams adopting Copilot.”

# GitHub Copilot Workshop

> **Get your team on board with GitHub Copilot through hands-on exercises that teach the Plan → Agent → Review workflow.**

Most teams adopt Copilot as a fancy autocomplete. That misses the point. The real unlock is learning to **collaborate with Copilot as a thinking partner** — directing it with Planning Mode, executing with Agent Mode, and reviewing its work critically. This workshop teaches exactly that.

> **Completely new to Copilot?** Start with the [Beginner's Guide](docs/beginners-guide.md) — a gentle 5-minute introduction before diving into the workshop.

---

## Table of Contents

- [GitHub Copilot Workshop](#github-copilot-workshop)
  - [Table of Contents](#table-of-contents)
  - [Philosophy](#philosophy)
  - [Prerequisites](#prerequisites)
  - [Workshop Structure](#workshop-structure)
    - [Facilitation Tips](#facilitation-tips)
  - [The Two Modes That Matter](#the-two-modes-that-matter)
    - [Planning Mode](#planning-mode)
    - [Agent Mode](#agent-mode)
  - [How to Write Good Planning Prompts](#how-to-write-good-planning-prompts)
    - [1. Context — What exists already?](#1-context--what-exists-already)
    - [2. Constraints — What are the boundaries?](#2-constraints--what-are-the-boundaries)
    - [3. Desired Outcome — What should the end result look like?](#3-desired-outcome--what-should-the-end-result-look-like)
  - [How to Review Agent Mode Output](#how-to-review-agent-mode-output)
    - [Review Checklist](#review-checklist)
    - [When to Push Back](#when-to-push-back)
  - [Rules of Engagement](#rules-of-engagement)
  - [Examples](#examples)
  - [Running the Workshop](#running-the-workshop)
    - [Before the Workshop](#before-the-workshop)
    - [During the Workshop](#during-the-workshop)
    - [After the Workshop](#after-the-workshop)
  - [Growing Adoption — One Week at a Time](#growing-adoption--one-week-at-a-time)
    - [Run the Workshop Weekly](#run-the-workshop-weekly)
    - [How You'll Know It's Working](#how-youll-know-its-working)
    - [When to Stop the Weekly Sessions](#when-to-stop-the-weekly-sessions)
  - [License](#license)

---

## Philosophy

Copilot's value isn't autocomplete — it's a **collaborative partner** you direct via Planning Mode and execute with via Agent Mode.

The passive approach — writing one big prompt, accepting everything, shipping without review — leads to code nobody understands and nobody can maintain. The active approach — planning incrementally, reviewing each step, building understanding as you go — makes you faster **and** keeps you in control.

This workshop teaches the active approach through three progressive hands-on examples.

## Prerequisites

| Requirement | Details |
|---|---|
| **VS Code** | Latest stable version |
| **GitHub Copilot** | Active Copilot subscription (Individual, Business, or Enterprise) |
| **Copilot Chat** | GitHub Copilot Chat extension installed in VS Code |
| **Python** | 3.10 or higher |
| **pip** | For installing dependencies (`pip install -r requirements.txt`) |
| **Git** | For cloning this repo |
| **Internet access** | Examples call public APIs |

## Workshop Structure

**Total time: ~2.5 hours**

| Phase | Duration | Focus |
|---|---|---|
| **Intro & Live Demo** | 20 min | Facilitator demonstrates the Plan → Agent → Review cycle on a live example |
| **Example 1: API Explorer** | 30 min | Write your first Planning Mode prompt, execute with Agent Mode |
| **Example 2: Data Transformer** | 30 min | Iterate on a plan, steer Agent Mode, ask Copilot to explain code |
| **Example 3: CLI Tool** | 45 min | Full Plan → Agent → Review → Refine cycle on a multi-file project |
| **Retrospective** | 15 min | What worked? What surprised you? Adoption next steps |

### Facilitation Tips

- **Group size**: 4–15 people. Larger groups need helpers to unblock individuals.
- **Pair up beginners**: If someone has never used Copilot, pair them with someone who has.
- **Live demo first**: Before Example 1, demonstrate the full cycle yourself — let participants see the rhythm before they try it.
- **Encourage comparison**: During examples, ask participants to share their prompts and Copilot's plans. Different prompts create different plans — that's the lesson.
- **Don't rush Example 3**: This is where the real learning happens. Give extra time if needed.

## The Two Modes That Matter

### Planning Mode

Planning Mode is how you tell Copilot **what you want to build** before any code is written. Think of it as writing a brief for a contractor — the clearer your brief, the better the result.

**When to use it:**
- Starting a new feature or script
- Tackling a problem you're not sure how to approach
- When you want Copilot to think through the approach before coding

**How it works:**
1. Open Copilot Chat in VS Code
2. Describe what you want to build — include context, constraints, and desired outcome
3. Copilot produces a step-by-step plan
4. You review the plan, refine it, then approve it for execution

> 📖 **Deep dive**: [Planning Mode Guide](docs/planning-mode-guide.md)

### Agent Mode

Agent Mode is how you let Copilot **execute the plan** — it reads files, writes code, runs commands, and creates tests. Think of it as a junior developer working from your approved plan.

**When to use it:**
- After you've reviewed and approved a plan
- For implementing well-defined, scoped pieces of work
- When you want Copilot to handle the mechanical parts while you focus on review

**How it works:**
1. Approve the plan from Planning Mode (or describe the task directly)
2. Copilot works autonomously — editing files, running commands, creating code
3. You review each change as it happens
4. You accept, reject, or redirect as needed

> 📖 **Deep dive**: [Agent Mode Guide](docs/agent-mode-guide.md)

## How to Write Good Planning Prompts

The quality of Copilot's plan directly depends on the quality of your prompt. A good planning prompt has three parts:

### 1. Context — What exists already?

> *"I have a Python project that reads device data from a REST API. The project uses `requests` for HTTP calls and `argparse` for CLI arguments."*

### 2. Constraints — What are the boundaries?

> *"Use only the standard library plus `requests`. No external frameworks. The script should be a single file under 200 lines."*

### 3. Desired Outcome — What should the end result look like?

> *"Create a CLI tool that accepts a search term, queries the API, and prints matching device names and IPs in a formatted table."*

**Common mistakes:**
- ❌ Too vague: *"Build me something that queries an API"*
- ❌ Too narrow: *"Write line 47 of the function"*
- ❌ No context: *"Add error handling"* (to what? for which errors?)
- ✅ Just right: *"Add error handling to the `query_devices` function for network timeouts and 401/403 auth errors. Log errors using the `logging` module at the ERROR level."*

> 📖 **Full guide with examples**: [Planning Mode Guide](docs/planning-mode-guide.md)

## How to Review Agent Mode Output

Treat Agent Mode output like a **pull request from a junior developer**. It's probably mostly right, but you need to check.

### Review Checklist

- [ ] **Does it follow the plan?** Compare the output to the approved plan step by step
- [ ] **Are there unnecessary changes?** Watch for files you didn't ask to be modified
- [ ] **Is the code readable?** Can you explain what every function does?
- [ ] **Are there hardcoded values** that should be configurable?
- [ ] **Is error handling appropriate?** Not too much, not too little
- [ ] **Are tests meaningful?** Do they test actual behavior, or just assert `True == True`?
- [ ] **Is it over-engineered?** Did Copilot add abstractions you don't need?
- [ ] **Security check**: No hardcoded secrets, no unsafe inputs, no unnecessary permissions

### When to Push Back

- The code is more complex than the task requires → *"Simplify this. I don't need a factory pattern for a single class."*
- Tests are superficial → *"These tests only check happy paths. Add tests for network errors and empty responses."*
- It modified files you didn't ask about → *"Revert changes to config.py. Only modify the query function."*

> 📖 **Full guide**: [Agent Mode Guide](docs/agent-mode-guide.md)

## Rules of Engagement

**Core principle: Copilot is your accelerator, not your replacement. You drive, Copilot assists. Develop gradually, review continuously.**

| ✅ DO | ❌ DON'T |
|---|---|
| Break work into small, reviewable steps | Write one massive prompt and accept everything |
| Review each piece before moving to the next | Skip reading the plan |
| Iterate on the plan — refine after each draft | Let Agent Mode run unchecked on large scopes |
| Read and understand generated code — you own it | Accept code you can't explain |
| Test generated code immediately | Accumulate large untested diffs |
| Ask Copilot to explain what you don't understand | Use Copilot as a crutch to avoid learning |
| Validate suggestions fit your architecture | Assume Copilot knows your conventions |

> 📖 **Full guide with "Develop Gradually" workflow**: [Rules of Engagement](docs/rules-of-engagement.md)

## Examples

| # | Title | Difficulty | Time | Copilot Focus |
|---|---|---|---|---|
| 1 | [API Explorer](examples/example_1_api_explorer/instructions.md) | Beginner | ~30 min | First planning prompt, first Agent Mode execution |
| 2 | [Data Transformer](examples/example_2_data_transformer/instructions.md) | Intermediate | ~30 min | Iterating on plans, steering Agent Mode, asking for explanations |
| 3 | [Professional CLI Tool](examples/example_3_cli_tool/instructions.md) | Advanced | ~45 min | Full Plan → Agent → Review → Refine cycle |

Each example follows the same workflow:
1. **Plan** — Write a prompt in Planning Mode
2. **Execute** — Let Agent Mode implement the plan
3. **Review** — Critically review the output
4. **Refine** — Iterate and improve

## Running the Workshop

### Before the Workshop

1. **Clone this repo** and ensure all participants have access:
   ```bash
   git clone https://github.com/tomas-ronec/github-copilot-workshop.git
   cd github-copilot-workshop
   pip install -r requirements.txt
   ```
2. **Verify Copilot works** for all participants — open VS Code, open Copilot Chat, send a test message.
3. **Prepare your live demo** — practice the Plan → Agent → Review cycle on a simple task (e.g., "create a Python script that prints the current weather from a public API"). The demo should take ~5 minutes.
4. **Print or share** the [Rules of Engagement](docs/rules-of-engagement.md) — participants should have this visible throughout.

### During the Workshop

1. **Intro (20 min)**: Explain the philosophy, run your live demo, walk through the Rules of Engagement.
2. **Example 1 (30 min)**: Everyone works through the API Explorer. Encourage sharing prompts.
3. **Example 2 (30 min)**: Data Transformer — emphasize reviewing and refining. Ask: *"What did Copilot get wrong? How did you fix it?"*
4. **Example 3 (45 min)**: CLI Tool — full cycle. Let participants work at their own pace.
5. **Retro (15 min)**: Ask each participant to share one thing that surprised them and one thing they'll use at work.

### After the Workshop

- Share the repo link for future reference
- Point teams to the [Rules of Engagement](docs/rules-of-engagement.md) as their daily guide


## Growing Adoption — One Week at a Time

One workshop isn't enough to change how a team works. Real adoption happens through **repetition and practice** — like learning any skill. The goal isn't perfection on day one; it's steady, visible growth in comfort and confidence.

### Run the Workshop Weekly

Repeat this workshop once a week until the team naturally reaches for Copilot in their daily work. Each session:

1. **Rotate the presenter.** Every week, a different team member drives the workshop — running the live demo, guiding the group through examples, and answering questions. Presenting builds deeper understanding, and it signals that Copilot isn't one person's tool — it's the team's.
2. **Everyone else follows along independently.** Participants work through the examples at their own pace, not just watching. Hands-on practice is where the learning happens.
3. **Start the retro with wins.** Ask: *"What did you use Copilot for this week that saved you time?"* Celebrate small victories — a test generated faster, a boilerplate script that took 5 minutes instead of 30.
4. **Keep it lightweight.** The weekly session doesn't need to be 2.5 hours every time. After the first full workshop, a 30–45 minute session focusing on one example or a real-world task from the team's backlog is enough.

### How You'll Know It's Working

You won't need metrics dashboards. You'll see it in the team's rhythm:

- **People start sharing prompts** — "Hey, try asking Copilot this way, I got better results"
- **Reviews get sharper** — team members spot over-engineering or missing error handling in Copilot output
- **Delivery feels smoother** — boilerplate, tests, and repetitive tasks stop being bottlenecks
- **New presenters are confident** — when someone who was hesitant in week 1 drives the workshop in week 4, that's real adoption
- **Copilot becomes invisible** — it's just part of how the team works, not a separate "thing"

### When to Stop the Weekly Sessions

Stop when the team no longer needs the structure — when using the Plan → Agent → Review workflow is second nature and people are helping each other naturally. Don't give up on slower adopters. Have patience and continue the workshops even with smaller number of participants.

After that, keep this repo as a reference and use it to onboard new team members.

---

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.
