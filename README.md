
A simple tool that enhances `uv init` by adding useful configuration to your `pyproject.toml`.

## What it does

After `uv init` creates a basic Python project, `chimechipmunk` automatically adds:

- **Ruff configuration** with comprehensive linting rules
- **Pyright configuration** for type checking with proper venv setup
- Additional tooling configuration (more coming soon)

## Usage

```bash
# Create a new project with uv
uv init --python=3.12 --package .

# Enhance it with chimechipmunk
chimechipmunk
```

That's it! Your `pyproject.toml` will be updated with sensible defaults for modern Python development.

## Installation

```bash
# Install chimechipmunk (installation method TBD)
pip install chimechipmunk
```

## What gets added

Currently adds to your `pyproject.toml`:

```toml
[tool.ruff]
preview = true

[tool.ruff.lint]
select = ["F", "E", "W", "C90", "I", "N", "UP", "YTT", "ASYNC", "ASYNC1", "S", "FBT", "B", "A", "C4", "DTZ", "T10", "DJ", "EM", "EXE", "FA", "ISC", "ICN", "LOG", "G", "INP", "PIE", "T20", "PYI", "PT", "Q", "RSE", "RET", "SLF", "SLOT", "SIM", "TID", "INT", "ARG", "PTH", "TD", "FIX", "ERA", "PD", "PL", "C", "R", "TRY", "FLY", "NPY", "AIR", "RUF"]

[tool.pyright]
venvPath = "."
venv = ".venv"
```


