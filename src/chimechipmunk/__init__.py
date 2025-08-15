import argparse
import pathlib
import typing

import tomlkit


def add_ruff_config_to_toml(file_path: pathlib.Path) -> None:
    """Add ruff lint configuration to a pyproject.toml file."""
    # Read the existing TOML file
    with file_path.open(encoding="utf-8") as f:
        doc: tomlkit.TOMLDocument = tomlkit.parse(f.read())

    # Create the ruff configuration (removed COM812 to avoid formatter conflicts)
    ruff_lint_rules: list[str] = [
        "F",
        "E",
        "W",
        "C90",
        "I",
        "N",
        "UP",
        "YTT",
        "ASYNC",
        "ASYNC1",
        "S",
        "FBT",
        "B",
        "A",
        "C4",
        "DTZ",
        "T10",
        "DJ",
        "EM",
        "EXE",
        "FA",
        "ISC",
        "ICN",
        "LOG",
        "G",
        "INP",
        "PIE",
        "T20",
        "PYI",
        "PT",
        "Q",
        "RSE",
        "RET",
        "SLF",
        "SLOT",
        "SIM",
        "TID",
        "INT",
        "ARG",
        "PTH",
        "TD",
        "FIX",
        "ERA",
        "PD",
        "PL",
        "C",
        "R",
        "TRY",
        "FLY",
        "NPY",
        "AIR",
        "RUF",
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


def main() -> None:
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

    args: argparse.Namespace = parser.parse_args()
    file_path: pathlib.Path = pathlib.Path(args.file_path)

    if not file_path.exists():
        return

    if file_path.suffix != ".toml":
        pass

    # Default to all if no specific flags are provided
    if not (args.ruff or args.pyright or args.all):
        args.all = True

    if args.all or args.ruff:
        add_ruff_config_to_toml(file_path)
    if args.all or args.pyright:
        add_pyright_config_to_toml(file_path)
