# CI OS Matrix

Status: in_progress

## Goal

Run the test workflow on Linux, macOS, and Windows while covering both
`ATOMICL_NO_EXTENSIONS=0` and `ATOMICL_NO_EXTENSIONS=1`.

## Exit Criteria

- GitHub Actions test jobs run on `ubuntu-latest`, `macos-latest`, and
  `windows-latest`.
- The test workflow exercises both `ATOMICL_NO_EXTENSIONS=0` and
  `ATOMICL_NO_EXTENSIONS=1`.
- Packaging interprets `ATOMICL_NO_EXTENSIONS=0` as the accelerated path and
  `ATOMICL_NO_EXTENSIONS=1` as the pure-Python path.

## Context

- `origin/master` already added `ATOMICL_NO_EXTENSIONS`, but the current
  implementation treats the string `"0"` as truthy.
- The current CI workflow only runs tests on Linux, so macOS and Windows
  install/test paths are unverified.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [ ] Add a regression test for `ATOMICL_NO_EXTENSIONS=0/1` build-mode
  selection.
- [ ] Fix `setup.py` parsing for `ATOMICL_NO_EXTENSIONS`.
- [ ] Expand the GitHub Actions test matrix across operating systems and
  extension modes.
- [ ] Validate the affected test and lint flows.

## Notes / Findings

- Windows support in CI depends on the pure-Python fallback path being valid,
  because the native extension implementation is written against GCC/Clang
  `__atomic_*` builtins.
