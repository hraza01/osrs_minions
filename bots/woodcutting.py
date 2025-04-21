import asyncio

import click
import pyautogui as pyg


async def woodcutting_bot(*args, **kwargs):

    x1, y1 = kwargs.get("primary_coordinates")
    x2, y2 = kwargs.get("secondary_coordinates")

    # TODO: Implement a way to get these coordinates dynamically
    # log_coordinates_cols = [1050, 1090, 1132, 1175] # 4k
    log_coordinates_cols = [780, 824, 865, 907]  # 2k

    # log_coordinates_rows = [1060, 1096, 1133, 1168, 1203, 1240]
    log_coordinates_rows = [680, 718, 754, 788, 824, 860]

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            num_actions = 2

            for i in range(1, num_actions + 1):
                click.secho(
                    f"Action {i + i // 2} of {num_actions * 2}",
                    fg="bright_cyan",
                )
                pyg.moveTo(x1, y1, duration=0.75)
                pyg.click()
                await asyncio.sleep(34)

                click.secho(
                    f"Action {i + 1 + i // 2} of {num_actions * 2}", fg="bright_cyan"
                )
                pyg.moveTo(x2, y2, duration=0.75)
                pyg.click()
                await asyncio.sleep(34)

            pyg.keyDown("shift")
            for col in log_coordinates_cols:
                for row in log_coordinates_rows:
                    pyg.moveTo(col, row, duration=0.2)
                    pyg.click()
                    await asyncio.sleep(0.1)

            pyg.keyUp("shift")
            await asyncio.sleep(5)

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
