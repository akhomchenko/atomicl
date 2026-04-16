# No-Extensions Install Path

Status: in_progress

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
- [ ] Add tests that cover disabling extensions via environment variable.
- [ ] Update packaging to skip extension configuration when
  `ATOMICL_NO_EXTENSIONS=1` is set.
- [ ] Document the new install/build behavior and validate the touched flows.

## Notes / Findings

- The new environment-variable path should bypass extension configuration
  entirely instead of pretending the extension failed to compile.
