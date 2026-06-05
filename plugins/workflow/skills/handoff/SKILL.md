---
name: handoff
description: |
  Comprime a conversa atual em documento de handoff para outro agente continuar.
source: vendored
upstream: https://github.com/mattpocock/skills
license: MIT
argument-hint: "What will the next session be used for?"
added: 2026-05-16
vendored: 2026-06-05
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
