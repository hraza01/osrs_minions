import asyncio

import click

import bots
from events import setup_coordinates, start_abort_listener
from utils import run_bot_with_status, start_timer, track_mouse

BOTS = {
    "thieving": bots.thieving.thieving_bot,
    "magic": bots.magic.magic_bot,
    "woodcutting": bots.woodcutting.woodcutting_bot,
    "agility": bots.agility.agility_bot,
    "cooking": bots.cooking.cooking_bot,
    "crafting": bots.crafting.crafting_bot,
    "herblore": bots.herblore.herblore_bot,
    "ranging": bots.ranging.ranging_bot,
    "fishing": bots.fishing.fishing_bot,
    "fletching": bots.fletching.fletching_bot,
    "mining": bots.mining.mining_bot,
    "prayer": bots.prayer.prayer_bot,
    "combat": bots.combat.combat_bot,
    "construction": bots.construction.construction_bot,
    "smithing": bots.smithing.smithing_bot,
    "firemaking": bots.firemaking.firemaking_bot,
}


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    )
)
@click.option(
    "-b",
    "--bot-type",
    type=click.Choice(BOTS.keys(), case_sensitive=False),
    help="Type of bot to run.",
    required=True,
)
@click.option(
    "-r",
    "--resolution",
    type=click.STRING,
    help="Screen resolution for the bot.",
    default="2k",
)
@click.option(
    "-c",
    "--category",
    type=click.STRING,
    help="Bot category within skill type",
)
@click.option(
    "-p",
    "--primary-coordinates",
    nargs=2,
    type=(int, int),
    help="Screen coordinates for clicks.",
)
@click.option(
    "-s",
    "--secondary-coordinates",
    nargs=2,
    type=(int, int),
    help="Screen coordinates for clicks.",
)
@click.option(
    "-t", "--track", is_flag=True, help="Enable live coordinate tracking mode."
)
@click.option(
    "-w",
    "--wait-time",
    type=int,
    help="Number of seconds to wait before starting.",
)
@click.pass_context
def main(
    ctx, bot_type, primary_coordinates, secondary_coordinates, track, *args, **kwargs
):
    """A Personal OSRS bot and/or helper that assists you in leveling up your in-game skills."""
    if track:
        track_mouse()
        return

    if not primary_coordinates and not secondary_coordinates:
        primary, secondary = setup_coordinates()
        ctx.params.update(
            primary_coordinates=primary,
            secondary_coordinates=secondary,
        )

    bot = BOTS.get(bot_type.lower(), None)

    if not bot:
        raise ValueError(f"Invalid bot type: {bot_type}")

    click.secho("Press Ctrl-C to stop the program.", fg="bright_red", bold=True)
    start_timer(ctx.params.get("wait_time"))

    # TODO: Implement pause instead of aborting the program
    start_abort_listener()
    asyncio.run(run_bot_with_status(bot, **ctx.params))


if __name__ == "__main__":
    main()
