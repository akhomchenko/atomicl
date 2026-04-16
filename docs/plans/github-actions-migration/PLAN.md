# GitHub Actions CI Migration

Status: done

## Goal

Migrate repository validation from Travis CI to GitHub Actions using the
`uv`-based workflow established in the recent modernization work, covering lint
and test validation for pushes and pull requests.

## Exit Criteria

- A GitHub Actions workflow exists at `.github/workflows/ci.yml`.
- Pushes to `master` and pull requests trigger CI in GitHub Actions.
- CI runs `uv run flake8` on CPython `3.14`.
- CI runs `uv run pytest` on CPython `3.11`, `3.12`, `3.13`, and `3.14`.
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
- [x] Add a GitHub Actions CI workflow for lint and test validation.
- [x] Remove Travis CI configuration and references from tracked files.
- [x] Validate the workflow shape against the current local `uv` commands.
- [x] Fix clean-checkout `uv sync` so the GitHub Actions jobs can install the
  project from source.

## Notes / Findings

- The current local validation contract is `uv sync`, `uv run flake8`, and
  `uv run pytest`.
- Multi-version test validation should run in separate CI jobs via a matrix,
  matching the modernization note that cross-version runs should not share the
  same checkout state.
- The GitHub Actions migration keeps CI on `ubuntu-latest` and mirrors the
  documented `uv` commands directly instead of reintroducing `tox`.
- The repo-level `pytest` configuration already constrains discovery to the
  `tests` directory, so CI can use plain `uv run pytest` without hard-coding a
  test path.
