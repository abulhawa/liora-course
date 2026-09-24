# Liora course

This project uses [uv](https://docs.astral.sh/uv/) to manage Python and the local virtual environment.

```powershell
uv sync
uv run python -m pytest
uv run ruff check .
```

`uv sync` creates `.venv` and installs the development tools. Run `uv sync` again after pulling dependency changes. To activate the environment in PowerShell, run `.venv\Scripts\Activate.ps1`; activation is optional when using `uv run`.

On machines with Windows Application Control, Python may need to be installed in an approved location. If commands fail with `An Application Control policy has blocked this file`, ask your administrator to approve the Python installation or use an approved Python interpreter with `uv sync --python <path-to-python.exe>`.
