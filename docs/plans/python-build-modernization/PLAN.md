# Python/Build Modernization

Status: in_progress

## Goal

Migrate the project from the legacy setuptools/tox/requirements workflow to PEP 517 packaging with `uv`, while preserving the optional Cython extension and the runtime API.

## Exit Criteria

- `uv sync` provisions the development environment.
- `uv run pytest` works on the default interpreter.
- `uv run --python 3.11 -m pytest`, `3.12`, `3.13`, and `3.14` work for each supported version.
- `uv build` produces an sdist and wheel.
- The compiled extension path works.
- The package with the native extension can be built from the released sdist when Cython is present.
- The package with the native extension can be built from the released sdist when Cython is absent.
- The pure-Python fallback still imports and functions.

## Context

- Support policy for this modernization is CPython `3.11-3.14`.
- The build backend remains `setuptools.build_meta`.
- Cython stays in the build path for now.
- `tox` is removed; local and future CI workflows use direct `uv` commands instead.
- Unpublished development builds use the PEP 440 version `0.1.2.dev0`; release tagging moves to `0.1.2` later.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [x] Document the repo rule that a feature starts with `PLAN.md` and that later atomic commits must update it.
- [ ] Add `pyproject.toml` and migrate project metadata/tooling configuration.
- [ ] Keep the optional Cython extension build working with setuptools.
- [ ] Remove legacy config and dependency files (`tox`, requirements files, old setuptools metadata).
- [ ] Remove obsolete compatibility helpers for modern CPython support.
- [ ] Update tests for the optional-extension fallback contract.
- [ ] Refresh developer documentation for Python support and `uv` workflows.
- [ ] Validate sync, tests, and build with the new workflow.

## Notes / Findings

- The upstream repository now tracks planning guidance in `AGENTS.md` and `docs/plans/README.md`; live work belongs under `docs/plans/<feature>/PLAN.md`.
- Repo guidance was tightened to require `PLAN.md` as the first feature commit and to require each later atomic commit to update the same live plan.
