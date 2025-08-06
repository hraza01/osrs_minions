import asyncio
import random

import click
import pyautogui as pyg


async def mining_bot(*args, **kwargs):

    points = [
        [647, 712],
        [677, 684],
        [708, 712],
    ]

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            # random_point = random.choice(points)
            for point in points:
                pyg.moveTo(point[0], point[1], duration=0.33)
                pyg.click()
                await asyncio.sleep(1.17)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
