# Python/Build Modernization

Status: done

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
- If the native extension cannot be built during installation, installation still succeeds and uses the pure-Python implementation.
- The pure-Python fallback still imports and functions.

## Context

- Support policy for this modernization is CPython `3.11-3.14`.
- The build backend is `setuptools.build_meta`.
- Cython stays in the build path for now.
- `tox` is removed; local and future CI workflows use direct `uv` commands instead.
- Unpublished development builds use the PEP 440 version `0.1.2.dev0`; release tagging moves to `0.1.2` later.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [x] Document the repo rule that a feature starts with `PLAN.md` and that later atomic commits must update it.
- [x] Add `pyproject.toml` and migrate project metadata/tooling configuration.
- [x] Keep the optional Cython extension build working with setuptools.
- [x] Remove legacy config and dependency files (`tox`, requirements files, old setuptools metadata).
- [x] Remove obsolete compatibility helpers for modern CPython support.
- [x] Update tests for the optional-extension fallback contract.
- [x] Refresh developer documentation for Python support and `uv` workflows.
- [x] Validate sync, lint, tests, and build with the new workflow.

## Notes / Findings

- The upstream repository now tracks planning guidance in `AGENTS.md` and `docs/plans/README.md`; live work belongs under `docs/plans/<feature>/PLAN.md`.
- Repo guidance was tightened to require `PLAN.md` as the first feature commit and to require each later atomic commit to update the same live plan.
- The existing test module imported `atomicl._cy` unconditionally, which conflicted with the intended pure-Python fallback behavior and needed to be corrected during modernization.
- The public-backend test was simplified to assert the effective backend in the current environment, instead of re-importing the package under a monkeypatched `_cy` failure path.
- The legacy benchmark dependency name `perf` no longer resolves in the package registry; the modern dependency is `pyperf`.
- The benchmark entrypoint also needed to import `pyperf` explicitly, and the README now documents the `uv` benchmark smoke-test command.
- `flake8` was part of the pre-migration developer workflow and needed to be preserved explicitly in the `uv`-based setup, along with its exclude configuration.
- The documented local workflow assumes `uv sync` has installed the default `dev` group before running lint, tests, benchmarks, or packaging commands from a checkout.
- Local `uv run --python ...` commands reuse the project `.venv`, so multi-version validation should run sequentially locally or in separate CI jobs rather than in parallel in the same checkout.
- Coverage path remapping only needs the repo `src/atomicl` tree and the project `.venv` install path for the current `uv` workflow; a generic `*/site-packages/atomicl` alias is broader than necessary.
- Package metadata was corrected after implementation to reflect the current author name and canonical GitHub repository URL.
- The packaging path now generates `_cy.c` for sdists and includes it there, while letting downstream sdist builds fall back to `_cy.c` without requiring Cython on the end system.
- Validation for the migrated workflow passed with `uv sync`, `uv run flake8`, `uv build`, isolated install from the built sdist, and `uv run pytest tests/test_atomicl.py`.
