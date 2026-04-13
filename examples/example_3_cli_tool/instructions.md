# Example 3: Professional CLI Tool

> **Difficulty:** Advanced | **Time:** ~45 minutes | **Focus:** Full Plan → Agent → Review → Refine cycle on a multi-file project

---

## Objective

Execute the complete **Plan → Agent → Review → Refine** workflow on a realistic project. You'll write a comprehensive planning prompt, review a larger plan, let Agent Mode build a multi-component tool, critically review the output, and then iteratively improve it.

## The Task

Build a professional CLI tool called `device_query.py` that:
- Queries the [NetBox Demo](https://demo.netbox.dev/) API to search for network devices
- Accepts a search term as a CLI argument
- Supports optional `--url`, `--token`, and `--verbose` flags
- Uses `logging` for all output (no `print()`)
- Handles authentication, network errors, and empty results gracefully
- Is polished enough to share with a colleague

This is the **most complex example** — take your time.

---

## Step 1: Write a Comprehensive Planning Prompt

This task has multiple components (CLI, API, logging, error handling). Your planning prompt needs to cover all of them.

### Suggested Planning Prompt

> *"Create a professional Python CLI tool called `device_query.py` that queries the NetBox Demo API for network devices. Here are the complete requirements:*
>
> **CLI Interface (argparse):**
> - *Required positional argument: `search_term` — the device name (or partial name) to search for*
> - *Optional `--url` — base URL of the NetBox instance (default: `https://demo.netbox.dev/`)*
> - *Optional `--token` — API token for authentication*
> - *Optional `-v` / `--verbose` — enable debug-level logging*
>
> **Authentication:**
> - *If `--token` is provided, use it*
> - *If `--token` is not provided, try the `NETBOX_API_TOKEN` environment variable*
> - *If neither exists, log a critical error and exit with code 1*
>
> **API Call:**
> - *Query `{url}/api/dcim/devices/?name__ic={search_term}` (case-insensitive contains)*
> - *Send the token as `Authorization: Token {token}` header*
> - *Log the URL being queried at INFO level*
> - *Log the full response at DEBUG level (only visible with `--verbose`)*
>
> **Output:**
> - *For each matching device, print: `{name} — {primary_ip}` (or `{name} — No IP assigned` if primary_ip is null)*
> - *Show the total count of results*
>
> **Error Handling:**
> - *Catch `requests.exceptions.RequestException` for network errors*
> - *Handle 401/403 with a specific 'authentication failed' message*
> - *Handle any other non-200 status with a generic error message*
>
> **Code Structure:**
> - *Single file with functions: `parse_args()`, `query_devices(url, token, search_term)`, and a `main()` function*
> - *Use `logging.basicConfig()` with format `%(levelname)s: %(message)s`*
> - *Use `if __name__ == '__main__'` pattern"*

### Review the Plan Critically

Before approving, check:

- [ ] Does the plan have a clear step for each component (CLI, auth, API, output, errors)?
- [ ] Is the ordering logical? (parse args → resolve token → make request → display results)
- [ ] Is there anything over-engineered? (e.g., creating multiple files, adding a config class, building a test suite)
- [ ] Is anything missing? (e.g., the exit-with-code-1 behavior for auth failures)

Refine at least once:
- *"Don't create a separate module — keep it in a single file."*
- *"The plan mentions creating tests — skip that for now, I'll add tests later."*
- *"Add a `logging.info('Script finished.')` at the end of execution."*

---

## Step 2: Execute with Agent Mode

Let Agent Mode implement the approved plan. Since this is a larger task, pay attention to:

- **Does it create only one file?** You asked for a single file.
- **Is the function structure what you specified?** (`parse_args`, `query_devices`, `main`)
- **Does it use `logging` everywhere?** (No stray `print()` calls)

---

## Step 3: Structured Review

This is a larger piece of code than the previous examples. Use a structured review approach.

### Code Structure Review

- [ ] Is the code organized into the three requested functions?
- [ ] Is `parse_args()` clean — just argparse setup, no logic?
- [ ] Does `query_devices()` handle all three auth/error scenarios?
- [ ] Does `main()` tie everything together clearly?

### Security Review

- [ ] Is the token handled securely? (not logged at INFO level, only at DEBUG)
- [ ] Are there any hardcoded URLs, tokens, or credentials?
- [ ] Is user input handled safely?

### Error Handling Review

- [ ] Network error → logged as error, script exits cleanly
- [ ] 401/403 → specific message about authentication
- [ ] Other HTTP errors → generic error with status code
- [ ] No token found → critical log + exit code 1

### Logging Review

- [ ] Default level is INFO
- [ ] `--verbose` switches to DEBUG
- [ ] No `print()` statements remain
- [ ] Debug messages include full response data
- [ ] URL being queried is logged at INFO

---

## Step 4: Refine Iteratively

Now practice the **incremental improvement** workflow. Ask Copilot to add features one at a time:

### Improvement 1: Better Output Formatting

> *"Update the output to display results in a formatted table with columns for Name, IP, and Status. Use string formatting, not an external table library."*

Review the change. Is it cleaner? Accept it or ask for adjustments.

### Improvement 2: Result Count in Exit Message

> *"After displaying results, log the total count: 'Found {n} device(s) matching {search_term}.' If no results, log a warning: 'No devices found matching {search_term}.'"*

### Improvement 3 (Bonus): Retry Logic

> *"Add simple retry logic: if the API request fails due to a network error, retry once after 2 seconds. Log a warning on the first failure. If the retry also fails, log the error and exit."*

For each improvement:
1. Review the plan/change
2. Let Agent Mode implement it
3. Review the diff — did it change only what you asked?
4. Test the change

---

## Step 5: Test It

### Get an API Token

1. Go to [https://demo.netbox.dev/](https://demo.netbox.dev/)
2. Log in with `admin` / `admin`
3. Navigate to your username (top right) → API Tokens → Add a Token
4. Copy the token

### Run the Tool

```bash
# Set the token as an environment variable
export NETBOX_API_TOKEN="your_token_here"

# Basic search
python device_query.py router

# Verbose mode
python device_query.py switch --verbose

# Custom URL and token
python device_query.py leaf --url "https://demo.netbox.dev/" --token "your_token_here"

# Test the help
python device_query.py --help

# Test with no token set (should show auth error)
unset NETBOX_API_TOKEN
python device_query.py router
```

### What to Verify

- [ ] `--help` shows all arguments with descriptions
- [ ] Basic search returns device names and IPs
- [ ] `--verbose` shows the full API response
- [ ] Missing token shows a clear error message
- [ ] Wrong URL shows a network error
- [ ] No results shows a "not found" message

---

## Step 6: Reflect

This was the full cycle. Ask yourself:

1. **How did your planning prompt compare to Examples 1 and 2?** Was it more detailed? More structured?
2. **How many times did you iterate** on the plan before approving?
3. **Did the structured review** catch anything the quick review wouldn't have?
4. **How did the incremental improvements** feel compared to asking for everything upfront?
5. **Could you maintain this code?** Could a teammate understand it?

---

## Copilot Skills Practiced

| Skill | What You Did |
|---|---|
| Comprehensive planning prompt | Covered CLI, auth, API, output, errors, and code structure in one plan |
| Critical plan review | Checked for over-engineering, missing steps, and ordering |
| Structured code review | Used a checklist covering correctness, security, error handling, and logging |
| Iterative refinement | Added features one at a time after the initial implementation |
| Incremental testing | Tested after each change, not just at the end |

---

## Reference Solution

A reference implementation is provided in [solutions/device_query.py](solutions/device_query.py). Compare your Copilot-generated solution to it — but remember, there's no single "correct" answer. If your code works, is readable, and handles errors, it's a valid solution.

## Success Criteria

- [ ] Tool runs and returns results from the NetBox demo API
- [ ] All three CLI arguments work (`search_term`, `--url`, `--token`, `--verbose`)
- [ ] Token resolution works (CLI arg → env var → error)
- [ ] Error handling covers network errors, auth failures, and empty results
- [ ] All output uses `logging` (no `print()`)
- [ ] You iterated on the plan at least once
- [ ] You added at least one improvement after the initial implementation
- [ ] You can explain every function in the generated code
