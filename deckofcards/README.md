# Deck of Cards

Small learning project extracted from the main workspace.

[![Tests](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/<OWNER>/<REPO>/branch/main/graph/badge.svg?token=REPLACE_WITH_TOKEN)](https://codecov.io/gh/<OWNER>/<REPO>)

Install locally for development:

```bash
pip install -e ./deckofcards
```

Run tests:

```bash
pytest -q deckofcards/tests
```

Run tests with coverage locally:

```bash
pytest -q --cov=deckofcards --cov-report=xml:coverage.xml --cov-report=html:coverage_html
```

Upload coverage to Codecov from CI (optional):

1. Add `CODECOV_TOKEN` secret to your GitHub repository (not required for public repos).
2. CI will run pytest with coverage and upload `coverage.xml` to Codecov using the `codecov/codecov-action`.

Run the classic deck example (after install):

```bash
deck-classic
```
