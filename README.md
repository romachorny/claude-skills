# Claude Skills by GenVidPro

Agent skills from a one-person AI studio that runs video production, client outreach and business automation with Claude. Every skill here came out of real work: a process was done by hand, then with Claude, and only when it ran without friction it was packed into a `SKILL.md`.

Works with Claude Code, Claude.ai / Cowork and the Claude API (any agent that reads the Agent Skills format).

## Skills

| Skill | Area | What it does |
|---|---|---|
| [animating-classical-paintings](skills/animating-classical-paintings/SKILL.md) | Creative tech | Living paintings: two modes, license check, anti-stuck protocol, eight acceptance rules, prompt template |
| [frame-by-frame-video-qa](skills/frame-by-frame-video-qa/SKILL.md) | Video production | Accept or reject a generated clip by numbers: motion map, 6x6 energy grid, loop seam, brightness drift. Includes `qa.py` |
| [hebrew-rtl-copy-blocks](skills/hebrew-rtl-copy-blocks/SKILL.md) | Localization (Israel) | Hebrew that reads right in chat code blocks and copy boxes: direction marks on every line plus layout rules. Includes `rtl_wrap.py` |
| [human-outreach-voice](skills/human-outreach-voice/SKILL.md) | Sales | Messages that sound like a busy human, in English, Hebrew and Russian, plus a fix for broken Hebrew RTL in copy blocks |
| [agent-browser-etiquette](skills/agent-browser-etiquette/SKILL.md) | Agents | Browsing under a real person's accounts without getting them banned |
| [agent-task-handoff](skills/agent-task-handoff/SKILL.md) | Agents | Handing tasks between Claude Code sessions on a server, a repo and a laptop, verified against the drive |
| [action-step-format](skills/action-step-format/SKILL.md) | Implementation | Replies for an owner who listens by voice: decisions first, numbered steps, where-to-paste lines |

More skills are being cleaned of private details and added.

## Install

**Claude Code**

```bash
git clone https://github.com/romachorny/claude-skills.git
cp -r claude-skills/skills/<skill-name> ~/.claude/skills/
```

**Claude.ai / Cowork:** zip a skill folder and upload it in Settings, Capabilities, Skills.

## How a skill is born here

1. Do the task by hand and understand your own algorithm.
2. Do it together with Claude until it runs without friction.
3. Ask Claude to describe the whole process you just went through, with your criteria and what you disliked, and turn it into a skill.
4. Every lesson from a failure goes back into the skill the same day.

## How this is built

Ideas, product decisions and creative direction by Roman Chorny ([GenVidPro](https://genvidpro.com)). Text and code written together with Claude.

## License

MIT
