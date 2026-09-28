---
name: agent-task-handoff
description: How a planning agent hands work to a coding agent running elsewhere (a 24/7 server, a cloud repo session, a laptop) - two copy blocks, a session rename with a location prefix and one self-contained English task, verified against the shared drive and not against the agent's own report. Use whenever a task must run in another Claude Code session.
---

# Agent task handoff

A system with several places where Claude Code runs gets messy fast: nobody remembers which session did what, and "done" in a report is not always done on disk. This format fixes both.

## Places

Name every place with a short uppercase prefix, for example:

- `SERVER` a 24/7 machine: bots, workflows, deploys, the always-on browser.
- `REPO` a cloud session on top of a repository. Changes land on the server only after pull or deploy.
- `LAPTOP` the owner's computer. Keep new work off it when possible.

## Hand-off: always two blocks, at the end of the reply

1. Session name, the first thing pasted into the new session:
```
/rename SERVER · <short task name in English>
```
2. The task itself: English, one piece, self-contained, no questions about small things. It must say what "done" means and where the proof lives.

Above the blocks, one line in the owner's language: where to open the new session.

## Writing the task

- Context in two or three sentences: project path, what exists, what is broken.
- A numbered "Do" list.
- "Verify" section: check every claim against the shared source of truth (the drive, the live URL, the repo), not against the local file the agent just wrote. A result that is reported but not true on the drive is the failure this rule exists for.
- "Report" section: where the result file goes and its first line (a one-line verdict).
- Secrets never go into the task text. Point to where they are stored.

## Rules

- Names are 2 to 5 English words, no date unless it matters.
- If `/rename` does not work: session menu, Rename, same name.
- Do not rename a session while it is still working.
- One owner per file: if the server owns a config, other agents only read it.
