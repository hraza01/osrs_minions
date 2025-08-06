import asyncio

import click
import pyautogui as pyg

from utils import generate_random_interval


async def cooking_bot(*args, **kwargs):

    fire = kwargs.get("primary_coordinates")
    bank = kwargs.get("secondary_coordinates")

    # 4k
    # cook_item = (395, 364)
    # deposit_all = (702, 1044)

    # 2k
    cook_item = (186, 206)
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
            pyg.moveTo(cook_item[0], cook_item[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            # press "esc"
            pyg.keyDown("esc")
            pyg.keyUp("esc")
            await asyncio.sleep(1)

            # click cook fire
            # press space to cook all
            # logic below makes sure that cooking notifications don't int cooking
            # cooking_round = 0

            # while cooking_round <= 2:
            pyg.moveTo(fire[0], fire[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            pyg.keyDown("space")
            pyg.keyUp("space")

            await asyncio.sleep(65)
            # cooking_round += 1

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
