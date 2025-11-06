
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
select = ["ALL"]
ignore = ["T201", "CPY001"]
[tool.pyright]
venvPath = "."
venv = ".venv"
```


