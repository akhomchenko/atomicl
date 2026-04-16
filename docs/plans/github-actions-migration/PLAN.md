# GitHub Actions CI Migration

Status: in_progress

## Goal

Migrate repository validation from Travis CI to GitHub Actions using the
`uv`-based workflow established in the recent modernization work, covering lint
and test validation for pushes and pull requests.

## Exit Criteria

- A GitHub Actions workflow exists at `.github/workflows/ci.yml`.
- Pushes to `master` and pull requests trigger CI in GitHub Actions.
- CI runs `uv run flake8` on CPython `3.14`.
- CI runs `uv run pytest tests/test_atomicl.py` on CPython `3.11`, `3.12`,
  `3.13`, and `3.14`.
- `.travis.yml` is removed.
- The README uses a GitHub Actions badge instead of a Travis badge.
- The changelog notes that CI moved from Travis CI to GitHub Actions.

## Context

- The repo's modernization work moved local and future CI workflows to direct
  `uv` commands and dropped `tox`.
- CI migration scope is validation only; packaging validation, release
  artifacts, and PyPI publishing are out of scope for this feature.
- The current default branch is `master`.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [ ] Add a GitHub Actions CI workflow for lint and test validation.
- [ ] Remove Travis CI configuration and references from tracked files.
- [ ] Validate the workflow shape against the current local `uv` commands.

## Notes / Findings

- The current local validation contract is `uv sync`, `uv run flake8`, and
  `uv run pytest tests/test_atomicl.py`.
- Multi-version test validation should run in separate CI jobs via a matrix,
  matching the modernization note that cross-version runs should not share the
  same checkout state.
