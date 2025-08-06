import asyncio

import click
import pyautogui as pyg

from utils import generate_random_interval


async def crafting_bot(*args, **kwargs):

    bank = kwargs.get("primary_coordinates")
    craft_item = kwargs.get("secondary_coordinates")

    # 4k
    # cook_item = (395, 364)
    # deposit_all = (702, 1044)

    # 2k
    deposit_all = (495, 886)
    chisel = (707, 798)
    craft_item_inv = (747, 800)

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

            pyg.moveTo(craft_item_inv[0], craft_item_inv[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            # while in bank - get your crafting item
            pyg.moveTo(craft_item[0], craft_item[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            # press "esc"
            pyg.keyDown("esc")
            pyg.keyUp("esc")
            await asyncio.sleep(1)

            # click chisel with ruby
            pyg.moveTo(chisel[0], chisel[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(0.25)

            # click chisel with ruby
            pyg.moveTo(craft_item_inv[0], craft_item_inv[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(1)

            pyg.keyDown("space")
            pyg.keyUp("space")

            await asyncio.sleep(50)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
