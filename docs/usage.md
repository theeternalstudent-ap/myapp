# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run myapp                          # production defaults
uv run --env-file .env myapp          # dev settings
```

Or as a Python module:

```bash
uv run python -m myapp
```

## Environment Variables

| Variable    | Default    | Description                          |
|-------------|------------|--------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`  | `app.log`  | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

## Log Format

Log lines use a compact format — no milliseconds, 3-char level abbreviations, pipe separators:

```
2025-03-15 14:22:01 | INF | myapp.app:main:42 | Hello from myapp!
```

Level abbreviations: `TRC` `DBG` `INF` `SUC` `WRN` `ERR` `CRT`
