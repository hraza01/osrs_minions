import asyncio

import click
import pyautogui as pyg


async def ranging_bot(*args, **kwargs):
    """
    This bot automates the agility training process in a game.
    It uses pyautogui to simulate mouse movements and clicks.
    """

    cannon_loc = kwargs.get("primary_coordinates")
    pouch = kwargs.get("secondary_coordinates")

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            attempt = 0
            while attempt <= 10:
                pyg.moveTo(cannon_loc[0], cannon_loc[1], duration=0.25)
                pyg.click()
                # await asyncio.sleep(15)
                attempt += 1
                await asyncio.sleep(0.5)

            pyg.moveTo(pouch[0], pouch[1], duration=0.25)
            pyg.click()
            attempt = 0

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
