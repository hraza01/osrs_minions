import asyncio

import click
import pyautogui as pyg


async def prayer_bot(*args, **kwargs):

    x1, y1 = kwargs.get("primary_coordinates")
    x2, y2 = kwargs.get("secondary_coordinates")

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            pyg.moveTo(x1, y1, duration=0.02)
            pyg.click()
            await asyncio.sleep(0.02)

            pyg.moveTo(x2, y2, duration=0.02)
            pyg.click()
            await asyncio.sleep(0.02)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
