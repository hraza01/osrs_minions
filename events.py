import click
from pynput import keyboard, mouse

PRIMARY_COORDINATES = None
SECONDARY_COORDINATES = None
STOP_PROGRAM = False
pressed_keys = set()


def setup_coordinates():
    global PRIMARY_COORDINATES, SECONDARY_COORDINATES

    get_click_position(on_primary_click)
    get_click_position(on_secondary_click)

    return PRIMARY_COORDINATES, SECONDARY_COORDINATES


def get_click_position(click_event):
    click.secho(
        "Please click anywhere on the screen to capture the coordinates.",
        fg="bright_yellow",
        blink=True,
    )
    with mouse.Listener(on_click=click_event) as listener:
        listener.join()


def on_primary_click(x, y, button, pressed):
    global PRIMARY_COORDINATES

    if pressed:
        click.secho(f"Mouse clicked at ({x}, {y})\n", fg="bright_cyan")
        PRIMARY_COORDINATES = (x, y)
        return False


def on_secondary_click(x, y, button, pressed):
    global SECONDARY_COORDINATES

    if pressed:
        click.secho(f"Mouse clicked at ({x}, {y})\n", fg="bright_cyan")
        SECONDARY_COORDINATES = (x, y)
        return False


def start_abort_listener():
    def on_press(key):
        global STOP_PROGRAM

        try:
            pressed_keys.add(key)
            if (
                keyboard.Key.ctrl_l in pressed_keys
                and keyboard.KeyCode.from_char("c") in pressed_keys
                and not STOP_PROGRAM
            ):
                STOP_PROGRAM = True
                print("\r\nCtrl-C detected. Stopping the bot...", flush=True)
                return False
        except AttributeError:
            pass

    def on_release(key):
        try:
            pressed_keys.discard(key)
        except KeyError:
            pass

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
