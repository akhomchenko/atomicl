Changelog
===

## [Unreleased]

### Changed
- modernized packaging and development workflow to `pyproject.toml` and `uv`
- updated supported CPython versions to `3.11` through `3.14`
- removed `tox` from the local workflow
- migrated CI from Travis CI to GitHub Actions

### Fixed
- preserved optional native-extension fallback behavior across Cython, generated C, and pure-Python paths

## [0.1.1] - 2018-11-13
## Added
- option to run benchmarks for specific implementation
- python 3.7 support
- wheels for linux and osx

### Fixed
- benchmarks to display more accurate results
- missing `abc` decorator for `compare_and_set`

### Removed
- python 3.3 support

## [0.1.0] - 2017-09-24
### Added
- initial implementation for CPython
- benchmarks
- tests
