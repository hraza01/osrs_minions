import asyncio

import click
import pyautogui as pyg


async def fishing_bot(*args, **kwargs):

    fishing_spot = kwargs.get("primary_coordinates")
    _ = kwargs.get("secondary_coordinates")

    # TODO: Implement a way to get these coordinates dynamically
    log_coordinates_cols = [1078, 1121, 1162, 1204]  # 4k
    # log_coordinates_cols = [665, 707, 747, 790]  # 2k

    log_coordinates_rows = [1196, 1232, 1266, 1303, 1339, 1375]
    # log_coordinates_rows = [835, 872, 908, 943, 979, 1014]

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            pyg.keyDown("shift")
            for col in log_coordinates_cols:
                for row in log_coordinates_rows:
                    pyg.moveTo(col, row, duration=0.2)
                    pyg.click()
                    await asyncio.sleep(0.1)

            pyg.keyUp("shift")
            await asyncio.sleep(1)

            pyg.moveTo(fishing_spot[0], fishing_spot[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(48)

            pyg.moveTo(fishing_spot[0], fishing_spot[1], duration=0.25)
            pyg.click()
            await asyncio.sleep(48)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
