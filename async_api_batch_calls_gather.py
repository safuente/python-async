"""
gather() function allows to execute many awaitables such as coroutines and tasks concurrently
We may use the asyncio.gather() function in situations where we may create many tasks or coroutines
up-front and then wish to execute them all at once and wait for them all to complete before continuing on.
It allows a group of awaitables to be treated as a single awaitable.
This allows:
- Executing and waiting for all awaitables in the group to be done via an await expression.
- Getting results from all grouped awaitables to be retrieved later via the result() method.
- The group of awaitables to be canceled via the cancel() method.
- Checking if all awaitables in the group are done via the done() method.
- Executing callback functions only when all tasks in the group are done.

ensure_future() is a method to create Task from coroutine
"""
import aiohttp
import asyncio
import time


start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))