"""
Car Spotter logic prototype.

This is the computer-only version of the FREE-WILi car spotting game.
It uses keyboard input for now, but the order matches the real FREE-WILi
hardware buttons.

FREE-WILi button order from top to bottom:
1. Red button    -> red car
2. Blue button   -> blue car
3. Green button  -> black car, because it will be marked black
4. Yellow button -> yellow car
5. Silver button -> silver car
"""

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
    if color not in counts:
        raise ValueError(f"Unknown color: {color}")

    counts[color] += 1
    history.append(color)
    print(f"Added one {color} car.")


def undo_last():
    """Undo the most recent car entry."""
    if not history:
        print("Nothing to undo.")
        return

    last_color = history.pop()
    counts[last_color] -= 1
    print(f"Undid one {last_color} car.")


def total_cars():
    """Return the total number of cars spotted."""
    return sum(counts.values())


def display_state():
    """Display the current car counts."""
    print("\n====================")
    print("     CAR SPOTTER")
    print("====================")

    for color in COLORS:
        print(f"{color.title():<8}: {counts[color]}")

    print("--------------------")
    print(f"Total   : {total_cars()}")
    print("====================")


def display_controls():
    """Display the keyboard controls for the prototype."""
    print("\nControls match the FREE-WILi button order:")
    print("r = red")
    print("b = blue")
    print("k = black")
    print("y = yellow")
    print("s = silver")
    print("z = undo last entry")
    print("q = quit")


def handle_choice(choice):
    """Handle one keyboard input choice."""
    if choice == "r":
        add_car("red")
    elif choice == "b":
        add_car("blue")
    elif choice == "k":
        add_car("black")
    elif choice == "y":
        add_car("yellow")
    elif choice == "s":
        add_car("silver")
    elif choice == "z":
        undo_last()
    else:
        print("Invalid choice. Try r, b, k, y, s, z, or q.")


def main():
    """Run the Car Spotter prototype."""
    print("Welcome to Car Spotter!")
    display_controls()

    while True:
        display_state()

        choice = input("\nYour choice: ").lower().strip()

        if choice == "q":
            print("\nFinal session:")
            display_state()
            print("Goodbye!")
            break

        handle_choice(choice)


if __name__ == "__main__":
    main()