# CI OS Matrix

Status: done

## Goal

Run the test workflow on Linux, macOS, and Windows.

## Exit Criteria

- GitHub Actions test jobs run on `ubuntu-latest`, `macos-latest`, and
  `windows-latest`.
- The workflow continues to exercise the existing test suite across all
  supported Python versions on each hosted runner.

## Context

- The current CI workflow only runs tests on Linux, so macOS and Windows
  install/test paths are unverified.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [x] Expand the GitHub Actions test matrix across hosted operating systems.
- [x] Validate the affected test and lint flows.

## Notes / Findings

- The native extension implementation is written against GCC/Clang
  `__atomic_*` builtins, so Windows CI must install with
  `ATOMICL_NO_EXTENSIONS=1` instead of attempting an accelerated build.
- Existing runtime tests already select both `_py` and `_cy` implementations
  when the extension imports successfully, so this plan only needs to expand
  OS coverage.
- Local validation on macOS passed with `uv run pytest`, `uv run ruff check`,
  and `uv run ruff format --check`.
