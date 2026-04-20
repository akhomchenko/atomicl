# C11 Stdatomic Migration

Status: in_progress

## Goal

Switch the native atomic implementation from compiler-specific GCC/Clang
extensions to the C11 `<stdatomic.h>` API, while preserving the current
runtime behavior and testing whether Windows CI can build the native extension
with MSVC's experimental C11 atomics support.

## Exit Criteria

- The native implementation uses C11 atomics instead of `__atomic_*` builtins.
- Local tests still pass on the current development toolchain.
- The build configuration requests C11 mode where needed for the native code.
- Windows CI is updated to attempt the native extension build with MSVC's
  experimental C11 atomics support instead of forcing pure Python.
- The plan records whether the Windows CI experiment succeeded or failed.

## Context

- The current C layer in `src/atomicl/_atomic.c` uses GCC-compatible
  `__atomic_*` builtins with sequentially consistent ordering.
- The current GitHub Actions workflow disables native extension builds on
  Windows by setting `ATOMICL_NO_EXTENSIONS=1`.
- Current Microsoft documentation still describes C-mode `<stdatomic.h>`
  support as experimental, but Visual Studio has a preview-only
  `/experimental:c11atomics` path that is worth trying in CI.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [ ] Migrate the C implementation to `<stdatomic.h>` with equivalent
  sequentially consistent semantics.
- [ ] Update build configuration to request C11 mode, including the Windows
  experiment flags.
- [ ] Validate lint/tests locally on the current toolchain.
- [ ] Update CI to attempt the native extension build on Windows and record the
  result.

## Notes / Findings

- Windows CI already runs across supported Python versions, so the native build
  experiment can be isolated to workflow configuration rather than adding a new
  job family.
- The native API only needs fetch-add, fetch-sub, exchange, and compare-exchange,
  all of which have direct C11 `<stdatomic.h>` equivalents.
