import argparse
import pathlib
import sys
import typing

import tomlkit


def add_ruff_config_to_toml(file_path: pathlib.Path) -> None:
    """Add ruff lint configuration to a pyproject.toml file."""
    # Read the existing TOML file
    with file_path.open(encoding="utf-8") as f:
        doc: tomlkit.TOMLDocument = tomlkit.parse(f.read())

    # Create the ruff configuration (removed COM812 to avoid formatter conflicts)
    ruff_lint_rules: list[str] = [
        "A",
        "AIR",
        "ARG",
        "ASYNC",
        "ASYNC1",
        "B",
        "C",
        "C4",
        "C90",
        "DJ",
        "DTZ",
        "E",
        "EM",
        "ERA",
        "EXE",
        "F",
        "FA",
        "FBT",
        "FIX",
        "FLY",
        "G",
        "I",
        "ICN",
        "INP",
        "INT",
        "ISC",
        "LOG",
        "N",
        "NPY",
        "PD",
        "PIE",
        "PL",
        "PT",
        "PTH",
        "PYI",
        "Q",
        "R",
        "RET",
        "RSE",
        "RUF",
        "S",
        "SIM",
        "SLF",
        "SLOT",
        "T10",
        "T20",
        "TD",
        "TID",
        "TRY",
        "UP",
        "W",
        "YTT",
    ]

    # Ensure [tool] section exists
    try:
        tool_section: typing.Any = doc["tool"]
    except KeyError:
        doc["tool"] = tomlkit.table()
        tool_section = doc["tool"]

    # Ensure [tool.ruff] section exists
    try:
        ruff_section: typing.Any = tool_section["ruff"]
    except KeyError:
        tool_section["ruff"] = tomlkit.table()
        ruff_section = tool_section["ruff"]

    # Add preview setting to [tool.ruff]
    ruff_section["preview"] = True

    # Ensure [tool.ruff.lint] section exists
    try:
        lint_section: typing.Any = ruff_section["lint"]
    except KeyError:
        ruff_section["lint"] = tomlkit.table()
        lint_section = ruff_section["lint"]

    # Add the select configuration
    lint_section["select"] = ruff_lint_rules

    # Write the modified TOML back to the file
    with file_path.open("w", encoding="utf-8") as f:
        f.write(tomlkit.dumps(doc))


def add_pyright_config_to_toml(file_path: pathlib.Path) -> None:
    """Add pyright configuration to a pyproject.toml file."""
    # Read the existing TOML file
    with file_path.open(encoding="utf-8") as f:
        doc: tomlkit.TOMLDocument = tomlkit.parse(f.read())

    # Ensure [tool] section exists
    try:
        tool_section: typing.Any = doc["tool"]
    except KeyError:
        doc["tool"] = tomlkit.table()
        tool_section = doc["tool"]

    # Ensure [tool.pyright] section exists
    try:
        pyright_section: typing.Any = tool_section["pyright"]
    except KeyError:
        tool_section["pyright"] = tomlkit.table()
        pyright_section = tool_section["pyright"]

    # Add pyright configuration
    pyright_section["venvPath"] = "."
    pyright_section["venv"] = ".venv"

    # Write the modified TOML back to the file
    with file_path.open("w", encoding="utf-8") as f:
        f.write(tomlkit.dumps(doc))


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Add configuration to pyproject.toml files"
    )
    parser.add_argument(
        "file_path",
        nargs="?",
        default="pyproject.toml",
        help="Path to the TOML file to modify (default: pyproject.toml)",
    )
    parser.add_argument(
        "--ruff",
        action="store_true",
        help="Add ruff lint configuration",
    )
    parser.add_argument(
        "--pyright",
        action="store_true",
        help="Add pyright configuration",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Add all configurations (ruff and pyright)",
    )

    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_args()
    file_path: pathlib.Path = pathlib.Path(args.file_path)

    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist", file=sys.stderr)
        sys.exit(1)

    if file_path.suffix != ".toml":
        print(
            f"Warning: File '{file_path}' does not have a .toml extension",
            file=sys.stderr,
        )

    # Default to all if no specific flags are provided
    if not (args.ruff or args.pyright or args.all):
        args.all = True

    if args.all or args.ruff:
        add_ruff_config_to_toml(file_path)
    if args.all or args.pyright:
        add_pyright_config_to_toml(file_path)
