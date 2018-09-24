#!/usr/bin/env python3

import asyncio
from concurrent.futures import ThreadPoolExecutor

async def request_ccxt(worker_func, n_workers, events, *args):

    result = {}

    with ThreadPoolExecutor(max_workers=n_workers) as executor:

        loop = asyncio.get_event_loop()
        futures = (
            loop.run_in_executor(
                executor, 
                worker_func, 
                i, 
                *args
            ) 
            for i in events
        )
        for resp in await asyncio.gather(*futures):
            result[resp[0]] = resp[1]

    return result

def run_loop(worker_func, n_workers, events, *args):
    loop = asyncio.get_event_loop()

    return loop.run_until_complete(
        request_ccxt(
            worker_func, 
            n_workers, 
            events,
            *args
        )
    )
