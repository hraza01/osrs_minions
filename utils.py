import asyncio
import time

import click
from pyautogui import displayMousePosition


def track_mouse():
    click.secho("Live mouse tracking is ON.", fg="bright_yellow")
    displayMousePosition()


def start_timer(wait_time):
    if wait_time is None:
        wait_time = 3
    for i in range(wait_time, 0, -1):
        print(f"Starting in {i}" + " " * 5, end="\r", flush=True)
        time.sleep(1)

    print(" " * 40, flush=True)


async def show_status(*args, **kwargs):

    click.secho(
        f"\rLaunching {kwargs.get('bot_type')} bot.\n",
        fg="bright_green",
        nl=False,
    )

    await asyncio.sleep(0.5)

    while True:
        from events import STOP_PROGRAM

        if not STOP_PROGRAM:
            for cursor in "\\|/-":
                click.secho(
                    f"\r{cursor} In Progress",
                    fg="bright_yellow",
                    nl=False,
                    blink=True,
                )
                await asyncio.sleep(0.15)
        else:
            break


async def run_bot_with_status(bot, **params):
    status_task = asyncio.create_task(show_status(**params))
    bot_task = asyncio.create_task(bot(**params))
    await asyncio.gather(
        status_task,
        bot_task,
    )


def get_cli_context(ctx):
    context = dict()
    for item in ctx.args:
        if "=" in item:
            key, value = item.split("=")
            context[key] = value

    return context
