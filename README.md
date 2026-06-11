# Car Tracker / Car Spotter

A small handheld FREE-WILi game for spotting cars by color during a trip.

This project is not meant to be an automated GPS vehicle tracker. The first version is a simple physical-button counting game: when you see a car, press the button that matches its color. The device shows current counts, total cars spotted, and eventually saves trip sessions and high scores.

## MVP

The first working version should do only four things:

1. Show counts for five car colors.
2. Increase a color count when its button is pressed.
3. Show the total number of cars spotted.
4. Save a finished session summary.

## Car colors

- Black
- Silver
- Blue
- Red
- Yellow

## Starting plan

Start with the Python prototype in `prototype/car_spotter_logic.py`. This lets the counting logic work before the FREE-WILi hardware code is added.

After the prototype works, move the same logic into `freewili-app/` and connect it to the FREE-WILi buttons, screen, LEDs, audio, and storage.

## Project folders

```text
assets/
  images/       Placeholder folder for screen graphics and icons.
  sounds/       Placeholder folder for button sounds and milestone sounds.
prototype/      Computer-only game logic prototype.
freewili-app/   Future FREE-WILi device implementation.
```

## First milestone

A working counter:

```text
CAR SPOTTER

Black: 0
Silver: 0
Blue: 0
Red: 0
Yellow: 0

Total: 0
```

Each button press increases one matching color.
