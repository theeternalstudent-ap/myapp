# myapp

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd myapp
uv sync
```

## Usage

Via the CLI entrypoint:

```bash
uv run myapp
```

With dev environment:

```bash
uv run --env-file .env myapp
```

Via Python module:

```bash
uv run python -m myapp
```

## Environment Variables

Copy `.env.example` to `.env` for development defaults:

```bash
cp .env.example .env
```

| Variable    | Default    | Description                                     |
|-------------|------------|-------------------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (set to DEBUG in `.env` for verbose output) |
| `LOG_FILE`  | `app.log`  | Path to the log file                            |

Load dev environment explicitly with `uv run --env-file .env` (uv does not auto-load `.env`).

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static docs:

```bash
uv run mkdocs build
```
