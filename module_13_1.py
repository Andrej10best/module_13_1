import asyncio

count_ball = 0

async def start_strongman(name, power):
    global count_ball
    local_count = count_ball
    print(f'Силач {name} начал соревнования.')
    while True:
        local_count += 1
        await asyncio.sleep(round(10 / power, 1))
        print(f'Силач {name} поднял {local_count} шар')
        if local_count == 5:
            print(f'Силач {name} закончил соревнования.')
            break


async def start_tournament():
    task_for_player_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_for_player_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_for_player_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task_for_player_1
    await task_for_player_2
    await task_for_player_3


asyncio.run(start_tournament())
