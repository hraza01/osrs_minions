import asyncio

import click
import pyautogui as pyg


async def firemaking_bot(*args, **kwargs):

    fire = kwargs.get("primary_coordinates")
    bank = kwargs.get("secondary_coordinates")

    # 4k
    # cook_item = (395, 364)
    # deposit_all = (702, 1044)

    # 2k
    logs_item = (234, 207)  # coordinates for logs in bank
    deposit_all = (495, 886)

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            # click bank, and deposit all items
            pyg.moveTo(bank[0], bank[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            pyg.moveTo(deposit_all[0], deposit_all[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            # while in bank - get your cooking item
            pyg.moveTo(logs_item[0], logs_item[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            # press "esc"
            pyg.keyDown("esc")
            pyg.keyUp("esc")
            await asyncio.sleep(1)

            # while cooking_round <= 2:
            pyg.moveTo(fire[0], fire[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            pyg.keyDown("space")
            pyg.keyUp("space")

            await asyncio.sleep(135)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
