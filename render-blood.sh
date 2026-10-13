#!/bin/sh
set -eu

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$PROJECT_DIR"

export PATH="$PROJECT_DIR/.venv/bin:$PATH"
export QUARTO_PYTHON="$PROJECT_DIR/.venv/bin/python"
export UV_CACHE_DIR="$PROJECT_DIR/.cache/uv"
export MPLCONFIGDIR="$PROJECT_DIR/.cache/matplotlib"
export JUPYTER_CONFIG_DIR="$PROJECT_DIR/.cache/jupyter/config"
export JUPYTER_DATA_DIR="$PROJECT_DIR/.cache/jupyter/data"
export JUPYTER_RUNTIME_DIR="$PROJECT_DIR/.cache/jupyter/runtime"
export IPYTHONDIR="$PROJECT_DIR/.cache/ipython"

mkdir -p "$MPLCONFIGDIR" "$JUPYTER_CONFIG_DIR" "$JUPYTER_DATA_DIR" \
  "$JUPYTER_RUNTIME_DIR" "$IPYTHONDIR"

uv sync --locked
quarto render bloodactividad/blood.qmd --to html "$@"
