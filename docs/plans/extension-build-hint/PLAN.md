# Extension Build Hint

Status: proposed

## Goal

Keep packaging on a single build path: accelerated installs either compile
successfully or fail, and pure-Python installs only happen when
`ATOMICL_NO_EXTENSIONS` is set explicitly.

## Exit Criteria

- Default installs attempt the native extension once and do not fall back to a
  second `setup()` invocation.
- A failed accelerated build exits with a clear hint to set
  `ATOMICL_NO_EXTENSIONS=1` for a pure-Python install.
- Setting `ATOMICL_NO_EXTENSIONS=1` still produces the explicit pure-Python
  install path.

## Context

- `origin/master` still retries `setup()` after a failed extension build.
- Editable installs can fail when setuptools re-enters the build pipeline after
  that first failure.
- The requested behavior is to drop the automatic fallback instead of retrying
  the build in a different mode.

## Tasks

- [ ] Create the live feature plan and use it as the execution tracker.
- [ ] Remove the automatic pure-Python fallback from `setup.py`.
- [ ] Add an actionable install hint for failed accelerated builds.
- [ ] Run the existing project checks against the updated packaging behavior.

## Notes / Findings

- No dedicated packaging/integration test module exists in the repository, so
  this work is expected to rely on the existing project validation commands plus
  targeted manual packaging-path checks if needed.
