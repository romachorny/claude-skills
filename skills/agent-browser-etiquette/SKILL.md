---
name: agent-browser-etiquette
description: Rules for an AI agent that browses under a real person's accounts - behave like a human, never risk a ban, keep pinned login tabs untouchable, stay off platforms that flag datacenter IPs, hand every login and captcha to the human, close your own tabs. Use in any task that opens a browser on someone's behalf.
---

# Agent browser etiquette

The agent works in a real browser with a real person's logins. A banned account costs more than any task, so speed is never worth the risk.

## 1. Where the browser runs

- **Visible browser first.** When the person is in the chat, work in the browser they can see, so they spot a login wall in five seconds instead of reading about it ten minutes later.
- **Server browser for unattended runs.** A 24/7 server browser is for scheduled jobs and when the person is away.
- **Check the exit IP once per session** before any sensitive platform (for example `ipinfo.io/json`). If it shows a datacenter instead of the person's usual residential or mobile network, do not open that platform. Say so in one line.

## 2. Platforms that punish datacenter logins

Marketplaces and social networks (freelance marketplaces, LinkedIn, Meta properties and similar) treat a login from a foreign datacenter as suspicious: a Cloudflare block before login, a frozen account, an identity check.

- Never open them from a datacenter browser.
- Learn about activity there from notification emails instead.
- See a block or a captcha: stop, do not retry, tell the human. Every retry hurts the IP's reputation.

## 3. Pinned tabs are untouchable

Keep the person's long-lived logins in pinned tabs (mail, messenger, hosting, repo host, automation tool).

- Never close them, never navigate them elsewhere, never use them for work.
- The login lives in the browser profile, not the tab. A new tab of your own on the same site is already logged in.
- Pin a new service only on the person's word.

## 4. Logins and captchas belong to the human

- The agent never types passwords, codes or tokens. It opens the login page and says one line: "log in here, tell me when done".
- Captchas and "Just a moment" checks are pressed by the human only.
- A site logged out during a scheduled run: do not log in, send one alert, do not repeat it while the issue stands.

## 5. Behave like a person on sites with the person's account

On service dashboards (hosting, repo host, automation tool) the agent may move fast. On sites where the person has a public identity:

- Pauses always different and never round: 3 to 8 s after a page load, 1.5 to 5 s between clicks, 4 to 12 s before Connect, Apply, Follow or Save, 15 to 60 s reading a profile or a job post.
- Click with the mouse at coordinates, sometimes hover first, not always dead centre. No scripted clicks.
- Scroll with the wheel in several moves, sometimes a bit past and back.
- Type in chunks of 15 to 40 characters with short pauses. Do not paste long text in one go.
- Navigate like a person: home or feed, then search or menu, then the page. One tab per platform. Sometimes look at notifications or the feed for 10 to 20 s.
- Work in series of 5 to 10 actions, then a 1 to 4 minute break. Shuffle the order of any list.
- Daily ceilings, then stop until tomorrow: for example 15 to 20 connection invites, 30 to 40 profile views, 10 to 15 new messages.
- Quiet hours at night in the person's time zone.
- Never send identical text to different people. Never scrape these platforms with scripts. Never be logged in to one platform from two places at once.

## 6. Clean up after every task

- Open your own tab for each page. Leave pinned tabs alone.
- The last step of every task or scheduled run: close every tab you opened.
- A run died halfway: on the next start, list the tabs first and close the leftovers.

## 7. Money and irreversible actions

Submit, Apply, Send, Publish, Pay, Delete are pressed by the human. The agent prepares everything up to that button and stops.
