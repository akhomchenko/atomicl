# Ruff Migration

Status: in_progress

## Goal

Replace Flake8 with Ruff for linting, formatting, and import sorting while
keeping the package runtime behavior and public API unchanged.

## Exit Criteria

- The development dependency set uses `ruff` instead of `flake8`.
- `pyproject.toml` contains the Ruff configuration needed for linting and
  import sorting.
- The README documents `uv run ruff check`, `uv run ruff check --fix`, and
  `uv run ruff format`.
- GitHub Actions runs `uv run ruff check` and `uv run ruff format --check`.
- Tracked Python files are Ruff-clean and Ruff-formatted.
- `uv run ruff check`, `uv run ruff format --check`, `uv run pytest`, and
  `uv build` all pass from a clean checkout.

## Context

- The repo currently documents and enforces `uv run flake8` locally and in CI.
- The project already declares `requires-python = ">=3.11,<3.15"`, so Ruff can
  infer the minimum supported Python version without an explicit
  `target-version`.
- The migration should follow Ruff defaults where practical, while enabling
  import sorting via the `I` rule family.
- Historical plan documents remain unchanged; this file is the only live
  tracker for the migration work.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [ ] Replace Flake8 with Ruff in development dependencies and configuration.
- [ ] Update the local workflow and CI documentation to use Ruff.
- [ ] Apply Ruff fixes, import sorting, and formatting to tracked Python files.
- [ ] Validate Ruff, tests, and build commands from the migrated workflow.

## Notes / Findings

- Baseline validation before migration passed with `uv run flake8` and
  `uv run pytest` (79 tests).
- Ruff defaults to `line-length = 88`, which the migration keeps by not
  setting an explicit line length.
- `ruff check` and `ruff format --check` are both required in CI because the
  formatter does not subsume linting.
