# AI Coding Instructions — Brooke Chauntel

## Copy this file to .github/copilot-instructions.md in any repo.

---

## Hard Rules (Never Break)

- Never commit secrets, API keys, tokens, wallet addresses, or credentials
- Never commit .env files — use .env.example with placeholders
- Never push directly to main — branch and PR only
- Never force-push a shared branch
- Never run destructive commands (rm -rf /, git reset --hard) without explicit confirmation

---

## Writing Style

Applies to all copy, alt text, comments, commit messages, and documentation.

### Banned words — replace with the plain alternative

**Verbs:** delve, leverage, foster, harness, facilitate, bolster, embark, enhance, elevate, showcase, utilize, optimize, streamline, empower, revolutionize, unlock, uncover, navigate (metaphorical)

**Adjectives:** robust (non-technical), seamless, crucial, vital, pivotal, multifaceted, nuanced, comprehensive, groundbreaking, transformative, cutting-edge, unprecedented, vibrant, dynamic, innovative

**Nouns/metaphors:** tapestry, landscape (figurative), realm, beacon, testament, journey (figurative), synergy, ecosystem (non-biological), paradigm, cornerstone

**Adverbs/transitions:** furthermore, moreover, additionally, notably, undeniably, ultimately, essentially, fundamentally, subsequently, diligently, meticulously

**Resume verbs:** established, ensured, maintained, positioned, spearheaded, championed, cultivated

**Significance inflators:** landmark, indelible, profound impact, sea change, pivotal moment

### Banned phrases — delete on sight

- "In today's fast-paced world…" → start with the actual point
- "In the ever-evolving landscape of…" → name the field
- "Let's dive in." / "Let's explore…" → just start
- "It's important to note that…" / "It's worth noting that…" → state the thing
- "Great question!" / "Absolutely!" / "Certainly!" → delete
- "I hope this helps!" → delete
- "Moving forward, we plan to…" → name the plan with a date, or delete
- "Going forward, we will…" → same
- "This positions us well for…" → name what specifically
- "Despite facing significant challenges… continues to thrive" → name the challenge and outcome
- "Through careful planning and iterative refinement…" → state what you built
- "Not only X but also Y" → list both directly
- "Everything from X to Y" → list what's actually included

### Core principles

- Be specific — numbers, names, examples over vague claims
- Prefer Anglo-Saxon words — "use" not "utilize", "help" not "facilitate"
- Repeat the right word — don't rotate synonyms to seem varied
- Name actors — "we shipped" not "the release was completed"
- Use contractions in informal text — "we've", "it's", "don't"
- Every paragraph needs at least one concrete anchor: a number, proper noun, or direct quote
- One point per paragraph; put the point near the top

---

## Coding Standards

- Read a file before editing it
- Follow the existing code style — don't reformat code outside the scope of the change
- No hardcoded secrets or personal data in source files
- No file over 400 lines, no function over 60 lines
- Error handling at system boundaries only
- Stage specific files — avoid git add .

### Commit messages

- Imperative mood, lowercase, under 72 chars — "add", "fix", "remove" not "added", "fixed"
- Subject names the specific thing changed and what was done
- Body (if used) explains why — the diff shows what
- Banned: "various", "several", "enhance", "improve code quality", "initial implementation" (except literal first commit)

### Comments

- Remove comments that restate what the code does
- Remove section headers inside functions: `# Setup`, `# Main logic`, `# Return result`
- Keep comments that explain why: external constraints, non-obvious decisions, workarounds

### Naming

- No type-narrating suffixes: `userDataObject` → `user`, `configSettings` → `config`
- No generic names: `result`, `data`, `info` — name what the value actually is
- In a class, don't repeat the class name in member names: `User.user_id` → `User.id`

### Tests

- Test names describe scenario + expected outcome: `test_expired_token_returns_401` not `test_auth`
- No `# Arrange`, `# Act`, `# Assert` comments — the code is the documentation

### Error messages

- Name the cause, not the symptom: `"user_id missing from session"` not `"An error occurred"`
