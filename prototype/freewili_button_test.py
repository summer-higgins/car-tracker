"""
FREE-WILi button test for Car Tracker.

Goal:
Confirm that Python can read the five physical FREE-WILi buttons.

Hardware order:
1. Red    -> red car
2. Blue   -> blue car
3. Green  -> black car
4. Yellow -> yellow car
5. Silver -> silver car
"""

from freewili import FreeWili


def main():
    print("Looking for FREE-WILi...")

    device = FreeWili.find_first().expect("Failed to find a FREE-WILi device")
    device.open().expect("Failed to open FREE-WILi")

    print("Connected.")
    print("Press each FREE-WILi button from top to bottom.")
    print("Press Ctrl+C to stop.\n")

    last_button_read = device.read_all_buttons().expect("Failed to read buttons")

    try:
        while True:
            buttons = device.read_all_buttons().expect("Failed to read buttons")

            for button_color, button_state in buttons.items():
                previous_state = last_button_read[button_color]

                if previous_state == button_state:
                    continue

                if button_state == 1:
                    print(f"{button_color.name} pressed")
                else:
                    print(f"{button_color.name} released")

            last_button_read = buttons

    except KeyboardInterrupt:
        print("\nStopping button test.")

    finally:
        device.close()
        print("Disconnected.")


if __name__ == "__main__":
    main()