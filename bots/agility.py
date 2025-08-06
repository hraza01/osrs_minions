import asyncio
import os

import click
import pyautogui as pyg

from utils import get_bot_config


async def agility_bot(*args, **kwargs):
    """
    This bot automates the agility training process in a game.
    It uses pyautogui to simulate mouse movements and clicks.
    """

    bot = os.path.basename(__file__).split(".")[0]
    bot_config = get_bot_config(bot)

    course = kwargs.get("category")
    resolution = kwargs.get("resolution", "2k")

    course_coordinates = bot_config.get(course, {}).get(resolution, [])

    print(course_coordinates)

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            for coord in course_coordinates:
                pyg.moveTo(coord[0], coord[1], duration=0.5)
                pyg.click()
                await asyncio.sleep(coord[2])

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
