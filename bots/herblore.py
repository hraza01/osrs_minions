import time

import click
import pyautogui as pyg

from utils import generate_random_interval


async def herblore_bot(*args, **kwargs):

    type = kwargs.get("category")

    if type == "mixing":
        await mixer(*args, **kwargs)
    elif type == "crushing":
        await crusher(*args, **kwargs)


def crusher(*args, **kwargs):
    from events import STOP_PROGRAM

    bank = kwargs.get("primary_coordinates")
    pestle_and_mortar = kwargs.get("secondary_coordinates")
    deposit_all = (664, 800)
    ingredient = (184, 205)
    inv_slot = (750, 1013)

    try:

        while True:
            if STOP_PROGRAM:
                break

            # bot logic
            # click bank, and deposit all items
            pyg.moveTo(bank[0], bank[1], duration=0.5)
            pyg.click()
            time.sleep(1)

            pyg.moveTo(deposit_all[0], deposit_all[1], duration=0.5)
            pyg.click()
            time.sleep(0.5)

            # withdraw ingredient
            pyg.moveTo(ingredient[0], ingredient[1], duration=0.5)
            pyg.click()
            time.sleep(0.5)

            # press "esc"
            pyg.keyDown("esc")
            pyg.keyUp("esc")
            time.sleep(0.75)

            # mixing iteration
            iteration = 0
            while iteration < 27:
                pyg.moveTo(pestle_and_mortar[0], pestle_and_mortar[1], duration=0.15)
                pyg.click()
                pyg.moveTo(inv_slot[0], inv_slot[1], duration=0.15)
                pyg.click()
                time.sleep(0.15)
                iteration += 1

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")


def mixer(*args, **kwargs):
    from events import STOP_PROGRAM

    bank = kwargs.get("primary_coordinates")
    deposit_all = (494, 887)
    first_ingredient = (234, 210)
    second_ingredient = (185, 206)
    first_inv = (708, 908)
    second_inv = (748, 910)

    try:

        while True:
            if STOP_PROGRAM:
                break

            # bot logic
            # click bank, and deposit all items
            pyg.moveTo(bank[0], bank[1], duration=0.25)
            pyg.click()
            time.sleep(1)

            pyg.moveTo(deposit_all[0], deposit_all[1], duration=0.25)
            pyg.click()
            time.sleep(0.5)

            # while in bank - get your cooking item
            # withdraw 14 of first ing and 14 of second ing
            pyg.moveTo(first_ingredient[0], first_ingredient[1], duration=0.25)
            pyg.click()
            time.sleep(0.5)

            pyg.moveTo(second_ingredient[0], second_ingredient[1], duration=0.25)
            pyg.click()
            time.sleep(0.5)

            # press "esc"
            pyg.keyDown("esc")
            pyg.keyUp("esc")
            time.sleep(0.75)

            # click on first item then click on second item - to use.
            # repeat
            pyg.moveTo(first_inv[0], first_inv[1], duration=0.25)
            pyg.click()
            pyg.moveTo(second_inv[0], second_inv[1], duration=0.25)
            pyg.click()
            time.sleep(1)
            pyg.keyDown("space")
            pyg.keyUp("space")

            # time.sleep(15) # default
            time.sleep(20)
            # time.sleep(10) # mixing herbs with vials

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
