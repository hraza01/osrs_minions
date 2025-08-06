import asyncio

import click
import pyautogui as pyg


async def fletching_bot(*args, **kwargs):

    primary = kwargs.get("primary_coordinates")
    secondary = kwargs.get("secondary_coordinates")

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            attempt = 0

            while attempt <= 50:
                pyg.moveTo(primary[0], primary[1], duration=0.1)
                pyg.click()

                pyg.moveTo(secondary[0], secondary[1], duration=0.1)
                pyg.click()
                attempt += 1

            await asyncio.sleep(5)
            attempt = 0

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
