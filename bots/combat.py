import time

import click
import pyautogui as pyg


async def combat_bot(*args, **kwargs):

    # rock cake
    primary = kwargs.get("primary_coordinates")

    overload_pots = [
        # [X, Y, POT_SIZE]
        [705, 800, 3],
        [748, 800, 4],
        [790, 800, 4],
        [665, 840, 4],
        [706, 840, 4],
        [748, 840, 4],
        [790, 840, 4],
    ]

    absorption_pots = [
        # [X, Y, POT_SIZE]
        # 1st row
        [665, 873, 4],
        [705, 873, 4],
        [748, 873, 4],
        [790, 873, 4],
        # 2nd row
        [665, 910, 4],
        [705, 910, 4],
        [748, 910, 4],
        [790, 910, 4],
        # 3rd row
        [665, 946, 4],
        [705, 946, 4],
        [748, 946, 4],
        [790, 946, 4],
        # 4th row
        [665, 982, 4],
        [705, 982, 4],
        [748, 982, 4],
        [790, 982, 4],
        # 5th row
        [665, 1018, 4],
        [705, 1018, 4],
        [748, 1018, 4],
        [790, 1018, 4],
    ]

    try:

        health_start_time = time.time()
        overload_start_time = time.time()
        absorption_start_time = time.time()

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # Your code block here
            time.sleep(4)  # run bot logic every 5 seconds

            current_time = time.time()

            health_elapsed_time = current_time - health_start_time
            overload_elapsed_time = current_time - overload_start_time
            absorption_elapsed_time = current_time - absorption_start_time

            click.clear()
            click.secho(
                f"""
                \r> Health Time Elapsed: {int(health_elapsed_time)} seconds\r
                \r> Overload Time Elapsed: {int(overload_elapsed_time)} seconds\r
                \r> Absorption Time Elapsed: {int(absorption_elapsed_time)} seconds\r
                """,
                fg="bright_white",
                nl=False,
            )

            if overload_elapsed_time >= 300:  # 301 seconds | 5 minutes + 1 second
                print("\nDrinking Overload Potion")

                overload_pot = []

                for pot in overload_pots:
                    # check if pot has a sip, take a sip, and reduce qty by 1
                    if pot[2] >= 1:
                        overload_pot = pot
                        pot[2] -= 1
                        break
                    else:
                        overload_pot = overload_pots[-1]

                print(overload_pot)
                pyg.moveTo(overload_pot[0], overload_pot[1], duration=0.25)
                pyg.click()
                time.sleep(6)

                # reset timer
                overload_start_time = time.time()

            if absorption_elapsed_time >= 105:  # sip every 65 seconds
                print("\nDrinking Absorption Potion")

                for pot in absorption_pots:
                    if pot[2] >= 1:
                        absorption_pot = pot
                        pot[2] -= 1
                        break
                    else:
                        absorption_pot = absorption_pots[-1]

                print(absorption_pot)
                pyg.moveTo(absorption_pot[0], absorption_pot[1], duration=0.25)
                pyg.click()

                # reset timer
                absorption_start_time = time.time()

            if health_elapsed_time >= 32.5:
                print("\nEating Rock Cake")
                pyg.moveTo(primary[0], primary[1], duration=0.25)
                pyg.click()
                time.sleep(0.5)
                pyg.click()
                time.sleep(1.5)

                # reset timer
                health_start_time = time.time()

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
