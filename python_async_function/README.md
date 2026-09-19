# Python - Async

A Holberton School back-end project covering asynchronous programming in Python with `asyncio`.

## Concepts

- `async` / `await` syntax
- Running coroutines concurrently
- `asyncio.as_completed` for collecting results in completion order
- Creating and managing `asyncio.Task` objects
- Measuring runtime with the `time` module

## Files

| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | `wait_random` coroutine: waits a random delay up to `max_delay` and returns it |
| `1-concurrent_coroutines.py` | `wait_n` coroutine: runs `wait_random` `n` times concurrently, returns delays in ascending order |
| `2-measure_runtime.py` | `measure_time` function: returns the average runtime per coroutine of `wait_n` |
| `3-tasks.py` | `task_wait_random` function: returns an `asyncio.Task` wrapping `wait_random` |
| `4-tasks.py` | `task_wait_n` coroutine: same as `wait_n` but built on `task_wait_random` |

## Usage

```bash
chmod +x *.py
./0-main.py
```

## Requirements

- Ubuntu 24.04
- Python 3.9+
- Code style checked with `pycodestyle`
- All files are executable and start with `#!/usr/bin/env python3`
- All functions and coroutines are type-annotated and documented
