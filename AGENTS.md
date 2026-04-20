# AGENTS.md

Follow any applicable system-level instructions and user-level instructions
(for example, a user-level `AGENTS.md`) first. Within the repository, follow
the most specific instructions that apply; treat this file as the default
repository-wide guidance unless a more specific repository-local file says
otherwise.

## Planning

Repository-specific plan guidance lives in [docs/plans/README.md](docs/plans/README.md).

- Track work in `docs/plans/<feature>/PLAN.md`.
- Use a stable human-readable slug for `<feature>` by default.
- If the human explicitly mentions a ticket or requests ticket-based naming, include the ticket in the directory name.
- Treat `docs/plans/<feature>/PLAN.md` as the only live planning document for that work.
- Start each feature by committing its `PLAN.md` first, before implementation commits.
- Keep implementation commits atomic and aligned to the plan.
- In each atomic implementation commit, update `docs/plans/<feature>/PLAN.md` so it is clear which task or finding that commit completed.
- Update `Tasks` and `Notes / Findings` in place while executing.
- Do not change `Goal` or `Exit Criteria` without human approval.

## Working On Code

- Do not include machine-specific absolute filesystem paths in checked-in files; prefer repository-relative paths and links when applicable.
- Keep `CHANGELOG.md` updated for public-facing changes such as supported Python version updates, new APIs, breaking changes, packaging changes, and behavior fixes; do not add internal-only implementation or process details. Follow the project's existing changelog structure and use https://keepachangelog.com/en/1.0.0/ as a guide.

## PRs

- Keep the PR title and body updated so they reflect the latest state of the branch before submission.
- Before submitting a PR, run two independent sub-agent reviews in rigorous review mode.
- Those review agents should have no context other than the PR title, PR body, and the actual changed files.
- Instruct both reviewers to challenge assumptions, verify backward compatibility, and confirm they agree with the PR description and the code as written.
