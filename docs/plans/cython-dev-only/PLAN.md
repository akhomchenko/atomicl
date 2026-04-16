# Cython Dev-Only Build Path

Status: done

## Goal

Make Cython a maintainer/developer packaging tool only, while ensuring that
release sdists include generated C sources and install without requiring
Cython, and preserving the optional native-extension fallback behavior.

## Exit Criteria

- Checkout packaging does not require Cython in `[build-system].requires`.
- uv packaging regenerates `src/atomicl/_cy.c` automatically when building from
  a checkout.
- Release sdists include generated `src/atomicl/_cy.c`.
- Developer workflows still install Cython by default through the `dev` group.
- Installing from the built sdist succeeds without depending on Cython in the
  isolated build environment.
- The repo docs and plan reflect the new packaging contract.

## Context

- The repo's current `setup.py` already supports building from `.pyx` when
  Cython is importable and from `.c` otherwise.
- The intended model is to keep Cython available for packaging from a checkout,
  while shipping generated C in the release sdist so downstream installs do not
  need Cython.
- uv can inject extra build dependencies for a specific package without
  publishing them as package metadata.

## Tasks

- [x] Create the live feature plan and use it as the execution tracker.
- [x] Configure the packaging tooling to inject Cython for checkout builds.
- [x] Remove Cython from non-dev packaging metadata where it is no longer
  required.
- [x] Validate local tests and sdist install behavior without Cython.

## Notes / Findings

- uv's `extra-build-dependencies` setting can provide Cython to the local build
  environment for `atomicl` without publishing Cython as a package build
  requirement.
- Validation should prove two separate behaviors: `uv` packaging from a checkout
  regenerates `_cy.c`, and a fresh `pip install` from the built sdist works
  without Cython.
