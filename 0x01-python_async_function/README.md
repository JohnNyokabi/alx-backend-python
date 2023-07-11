# 0x01. Python Async Function

## Requirements
        * Ubuntu OS
        * Python3
        * Pycodestyle

## Tasks    
    | Task | Details |
    | ---- | ------- |
    | 0-basic_async_syntax.py | Syntax for coroutine wait_random that computes async/await delay |
    | 1-concurrent_coroutines | Concurrent routine that spawns `wait_random` `n` times with the specified `max_delay` and returns list of all the delays sorted in ascending order as floats |
    | 2-measure_runtime.py | Function `measure_time`  that takes in `n` and `max_delay` as arguments for `wait_n(n, max_delay)` function to measure the total execution time |
    | 3-tasks.py | Function `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task` type" |
    | 4-tasks.py | Function `task_wait_n` that calls `task_wait_random` to return list of all delays sorted in ascending order |