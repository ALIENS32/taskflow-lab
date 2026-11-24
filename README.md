# Taskflow Lab

A simple Python command-line task management tool (`taskflow`).

## Features
- Add tasks (`taskflow add "Buy milk"`)
- List tasks (`taskflow list`)
- Mark tasks as completed (`taskflow done 1`)

## Development & Verification
```bash
PYTHONPATH=src python3 -m unittest discover -s tests
node --test .github/scripts/*.test.mjs
```
