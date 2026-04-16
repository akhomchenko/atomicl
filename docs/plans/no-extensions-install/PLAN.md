# No-Extensions Install Path

Status: done

## Goal

Allow installers to opt out of compiling the optional native extension by
setting `ATOMICL_NO_EXTENSIONS=1`, while preserving the existing compiled fast
path by default.

## Exit Criteria

- Installing or building with `ATOMICL_NO_EXTENSIONS=1` skips native-extension
  setup and produces a pure-Python install without relying on a compiler
  failure fallback.
- Default packaging behavior still attempts to build the optional native
  extension and retains the pure-Python fallback on compilation failure.
- Tests and docs cover the new environment-variable-controlled install path.

## Context

- The current packaging path always configures the extension first and only
  falls back to pure Python after a failed extension build.
- The project already ships both pure-Python and optional native-backed
  implementations, so the new work is strictly about packaging/build control.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [x] Validate the `ATOMICL_NO_EXTENSIONS=1` decision path without adding a
  dedicated `setup.py` test module.
- [x] Update packaging to skip extension configuration when
  `ATOMICL_NO_EXTENSIONS=1` is set.
- [x] Document the new install/build behavior and validate the touched flows.

## Notes / Findings

- `ATOMICL_NO_EXTENSIONS` now takes the package straight to the pure-Python
  `setup()` path instead of treating pure Python as a failed-extension fallback.
- The default path stays accelerated-first, using generated C by default,
  `cythonize(...)` when available, and the existing compile-failure fallback.
- `uv build` with isolated build dependencies could not be completed inside the
  sandbox because dependency resolution to PyPI was blocked by DNS/network
  restrictions, so validation used the runtime test suite plus a local manual
  packaging-path check.
