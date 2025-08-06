import asyncio

import click
import pyautogui as pyg


async def smithing_bot(*args, **kwargs):

    tasks = {
        "open_bank": [582, 723],
        "deposit_bars": [709, 802],
        "right_click_stamina_pot": [234, 210],
        "withdraw_stamina_pot": [178, 256],
        "right_click_pot_in_inventory": [709, 802],
        "drink_stamina_pot": [683, 937],
        "store_stamina_pot_in_bank": [709, 802],
        "withdraw_ores": [377, 205],
        "equip_smithing_gauntlets": [667, 803],
        "click_conveyor_belt": [301, 379],
        "click_waiting_tile": [377, 695],
        "put_on_ice_gloves": [667, 803],
        "click_collect_bars": [419, 551],
    }

    try:

        while True:
            from events import STOP_PROGRAM

            if STOP_PROGRAM:
                break

            # bot logic
            attempt = 0

            while attempt < 9:

                pyg.moveTo(tasks["open_bank"][0], tasks["open_bank"][1], duration=0.33)
                pyg.click()
                await asyncio.sleep(4.5)

                pyg.moveTo(
                    tasks["deposit_bars"][0], tasks["deposit_bars"][1], duration=0.33
                )
                pyg.click()
                await asyncio.sleep(1)

                if attempt == 0:
                    pyg.moveTo(
                        tasks["right_click_stamina_pot"][0],
                        tasks["right_click_stamina_pot"][1],
                        duration=0.33,
                    )
                    pyg.click(button="right")
                    await asyncio.sleep(1)

                    pyg.moveTo(
                        tasks["withdraw_stamina_pot"][0],
                        tasks["withdraw_stamina_pot"][1],
                        duration=0.33,
                    )
                    pyg.click()
                    await asyncio.sleep(1)

                    pyg.moveTo(
                        tasks["right_click_pot_in_inventory"][0],
                        tasks["right_click_pot_in_inventory"][1],
                        duration=0.33,
                    )
                    pyg.click(button="right")
                    await asyncio.sleep(1)

                    pyg.moveTo(
                        tasks["drink_stamina_pot"][0],
                        tasks["drink_stamina_pot"][1],
                        duration=0.33,
                    )
                    pyg.click()
                    await asyncio.sleep(1.2)

                    pyg.moveTo(
                        tasks["store_stamina_pot_in_bank"][0],
                        tasks["store_stamina_pot_in_bank"][1],
                        duration=0.33,
                    )
                    pyg.click()
                    await asyncio.sleep(1)

                pyg.moveTo(
                    tasks["withdraw_ores"][0], tasks["withdraw_ores"][1], duration=0.33
                )
                pyg.click()
                await asyncio.sleep(1)

                pyg.press("esc")

                pyg.moveTo(
                    tasks["equip_smithing_gauntlets"][0],
                    tasks["equip_smithing_gauntlets"][1],
                    duration=0.33,
                )
                pyg.click()
                await asyncio.sleep(1)

                pyg.moveTo(
                    tasks["click_conveyor_belt"][0],
                    tasks["click_conveyor_belt"][1],
                    duration=0.33,
                )
                pyg.click()
                await asyncio.sleep(8)

                pyg.moveTo(
                    tasks["click_waiting_tile"][0],
                    tasks["click_waiting_tile"][1],
                    duration=0.33,
                )
                pyg.click()
                await asyncio.sleep(6)

                pyg.moveTo(
                    tasks["put_on_ice_gloves"][0],
                    tasks["put_on_ice_gloves"][1],
                    duration=0.33,
                )
                pyg.click()
                await asyncio.sleep(1)

                pyg.moveTo(
                    tasks["click_collect_bars"][0],
                    tasks["click_collect_bars"][1],
                    duration=0.33,
                )
                pyg.click()
                await asyncio.sleep(2)

                pyg.press("space")
                await asyncio.sleep(1)

                attempt += 1

    except KeyboardInterrupt:
        click.secho("\nKeyboardInterrupt", fg="bright_white")
