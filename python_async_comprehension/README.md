# Python - Async Comprehension

A Holberton School back-end project covering async generators and async comprehensions in Python with `asyncio`.

## Concepts

- Async generators (`async def` with `yield`)
- Consuming them with `async for`
- Async comprehensions
- Running coroutines in parallel with `asyncio.gather`
- Measuring runtime with the `time` module

## Files

| File | Description |
|------|-------------|
| `0-async_generator.py` | `async_generator` coroutine: loops 10 times, waits 1 second each time, then yields a random number between 0 and 10 |
| `1-async_comprehension.py` | `async_comprehension` coroutine: collects 10 random numbers from `async_generator` using an async comprehension |
| `2-measure_runtime.py` | `measure_runtime` coroutine: runs `async_comprehension` four times in parallel with `asyncio.gather` and returns the total runtime |


