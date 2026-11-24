# Contributing to Taskflow Lab

## Code Quality & Verification
All PRs must pass:
1. `PYTHONPATH=src python3 -m unittest discover -s tests`
2. `node --test .github/scripts/*.test.mjs`
