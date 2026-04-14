# AGENTS.md

## Planning

Repository-specific plan guidance lives in [docs/plans/README.md](/Users/okhomchenko/src/python/atomicl/docs/plans/README.md).

- Track work in `docs/plans/<feature>/PLAN.md`.
- Use a stable human-readable slug for `<feature>` by default.
- If the human explicitly mentions a ticket or requests ticket-based naming, include the ticket in the directory name.
- Treat `docs/plans/<feature>/PLAN.md` as the only live planning document for that work.
- Start each feature by committing its `PLAN.md` first, before implementation commits.
- Keep implementation commits atomic and aligned to the plan.
- In each atomic implementation commit, update `docs/plans/<feature>/PLAN.md` so it is clear which task or finding that commit completed.
- Update `Tasks` and `Notes / Findings` in place while executing.
- Do not change `Goal` or `Exit Criteria` without human approval.
