# Planning Layout

This repository tracks work in a single live document per feature:

`/docs/plans/<feature>/PLAN.md`

That `PLAN.md` is both the design record and the execution board. Supporting files are allowed, but this is the only live execution tracker for the work.

## Feature Directory Naming

Use a stable human-readable slug for `<feature>` by default:

- `/docs/plans/overflow-semantics/PLAN.md`
- `/docs/plans/cpython-build-cleanup/PLAN.md`

If the human explicitly mentions a ticket or wants ticket-based naming, include it in the directory name:

- `/docs/plans/123-overflow-semantics/PLAN.md`

## Plan Ownership

Each feature `PLAN.md` is a live document.

- Agents should update `Tasks` and `Notes / Findings` while executing work.
- `Goal` and `Exit Criteria` are human-owned sections.
- Agents must not rewrite `Goal` or `Exit Criteria` without human approval.

## Default `PLAN.md` Shape

Use this structure unless the human asks for something else:

```md
# <Plan title>

Status: proposed | in_progress | done

## Goal

What should exist when this work is complete.

## Exit Criteria

- Observable condition that proves the work is complete
- Observable condition that proves the work is complete

## Context

Relevant background, constraints, and links.

## Tasks

- [ ] Concrete task
- [ ] Concrete task

## Notes / Findings

- Decision, discovery, blocker, or follow-up worth preserving during execution.
```

## Extra Files

Add extra files next to a feature `PLAN.md` only when the work actually needs them, for example:

- `research.md`
- `notes.md`
- `decisions.md`

Those files support the feature plan, but `docs/plans/<feature>/PLAN.md` remains the only live tracking document.
