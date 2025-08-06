import os
import time

import click
import pyautogui as pyg

from utils import generate_random_interval, get_bot_config


async def magic_bot(*args, **kwargs):

    category = kwargs.get("category")
    resolution = kwargs.get("resolution", "2k")

    bank = kwargs.get("primary_coordinates")
    item = kwargs.get("secondary_coordinates")

    bot = os.path.basename(__file__).split(".")[0]
    bot_config = get_bot_config(bot).get(category, {}).get(resolution, {})

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            if category == "high_alchemy":
                high_alchemy(bank, item, bot_config)
            elif category == "tan_hides":
                tan_hides(bank, item, bot_config)
            elif category == "degrime_herbs":
                degrime_herbs(bank, item, bot_config)
            else:
                click.secho(f"Unknown category: {category}", fg="red")
                return

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")


def high_alchemy(bank, item, bot_config):
    first_click_duration = generate_random_interval(0.25, 0.35)
    second_click_duration = generate_random_interval(0.25, 0.35)
    sleep_duration = generate_random_interval(1.65, 1.85)

    pyg.moveTo(bank[0], bank[1], duration=first_click_duration)
    pyg.click()

    pyg.moveTo(item[0], item[1], duration=second_click_duration)
    pyg.click()
    time.sleep(sleep_duration)


def tan_hides(bank, item, bot_config):
    d_item = bot_config.get("d_item", [])
    spell = bot_config.get("spell", [])

    first_click_duration = generate_random_interval(0.35, 0.45)
    second_click_duration = generate_random_interval(0.35, 0.45)

    pyg.press("num4")
    pyg.moveTo(bank[0], bank[1], duration=first_click_duration)
    pyg.click()
    time.sleep(0.55)

    pyg.moveTo(d_item[0], d_item[1], duration=second_click_duration)
    pyg.click()
    time.sleep(0.55)

    pyg.moveTo(item[0], item[1], duration=first_click_duration)
    pyg.click()
    time.sleep(0.6)

    pyg.keyDown("esc")
    pyg.keyUp("esc")
    time.sleep(1)

    pyg.keyDown("num6")
    time.sleep(0.5)

    pyg.moveTo(spell[0], spell[1], duration=second_click_duration)

    attempt = 0
    while attempt < 5:
        sleep_duration = generate_random_interval(1.26, 1.55)
        pyg.click()
        attempt += 1
        time.sleep(sleep_duration)


def degrime_herbs(bank, item, bot_config):
    d_item = bot_config.get("d_item", [])
    spell = bot_config.get("spell", [])

    first_click_duration = generate_random_interval(0.25, 0.45)
    second_click_duration = generate_random_interval(0.25, 0.45)

    pyg.moveTo(bank[0], bank[1], duration=first_click_duration)
    pyg.click()
    time.sleep(0.5)

    pyg.moveTo(d_item[0], d_item[1], duration=second_click_duration)
    pyg.click()
    time.sleep(0.5)

    pyg.moveTo(item[0], item[1], duration=first_click_duration)
    pyg.click()
    time.sleep(0.5)

    pyg.keyDown("esc")
    pyg.keyUp("esc")
    time.sleep(1)

    pyg.keyDown("num6")
    time.sleep(0.5)

    pyg.moveTo(spell[0], spell[1], duration=second_click_duration)
    pyg.click()
    time.sleep(6.5)
