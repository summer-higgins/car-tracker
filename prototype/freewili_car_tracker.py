"""
FREE-WILi Car Tracker / Car Spotter prototype.

This version uses the real FREE-WILi hardware buttons.

Confirmed FREE-WILi Python button names:
Red    -> red car
Blue   -> blue car
Green  -> black car
Yellow -> yellow car
White  -> silver car
"""

import time
from freewili import FreeWili


BUTTON_TO_CAR_COLOR = {
    "Red": "red",
    "Blue": "blue",
    "Green": "black",
    "Yellow": "yellow",
    "White": "silver",
}

COLORS = ["red", "blue", "black", "yellow", "silver"]

counts = {
    "red": 0,
    "blue": 0,
    "black": 0,
    "yellow": 0,
    "silver": 0,
}

history = []


def add_car(color):
    """Add one car to the selected color count."""
    counts[color] += 1
    history.append(color)
    print(f"{color.title()} car spotted!")


def undo_last():
    """Undo the most recent car entry."""
    if not history:
        print("Nothing to undo.")
        return

    last_color = history.pop()
    counts[last_color] -= 1
    print(f"Undid one {last_color} car.")


def total_cars():
    """Return total number of cars spotted."""
    return sum(counts.values())


def display_state():
    """Print the current tracker state to the laptop terminal."""
    print("\n====================")
    print("     CAR SPOTTER")
    print("====================")

    for color in COLORS:
        print(f"{color.title():<8}: {counts[color]}")

    print("--------------------")
    print(f"Total   : {total_cars()}")
    print("====================")


def handle_button_press(button_name):
    """Convert a FREE-WILi button press into a car color count."""
    car_color = BUTTON_TO_CAR_COLOR.get(button_name)

    if car_color is None:
        print(f"Ignored unknown button: {button_name}")
        return

    add_car(car_color)
    display_state()


def main():
    print("Looking for FREE-WILi...")

    device = FreeWili.find_first().expect("Failed to find a FREE-WILi device")
    device.open().expect("Failed to open FREE-WILi")

    print("Connected to FREE-WILi.")
    print("Press the hardware buttons to count cars.")
    print("Press Ctrl+C to stop.\n")

    display_state()

    last_button_read = device.read_all_buttons().expect("Failed to read buttons")

    try:
        while True:
            buttons = device.read_all_buttons().expect("Failed to read buttons")

            for button_color, button_state in buttons.items():
                previous_state = last_button_read[button_color]
                button_name = button_color.name

                # Count only the moment the button changes from released to pressed.
                if previous_state != button_state and button_state == 1:
                    handle_button_press(button_name)

            last_button_read = buttons
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nFinal session:")
        display_state()
        print("Stopping tracker.")

    finally:
        device.close()
        print("Disconnected.")


if __name__ == "__main__":
    main()
    