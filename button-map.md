# FREE-WILi Button Map

The FREE-WILi has five physical buttons arranged vertically. This project uses the physical button order as the source of truth.

## Hardware order

From top to bottom:

| Physical position | Button color on device | Project meaning |
| --- | --- | --- |
| 1 | Red | Red car |
| 2 | Blue | Blue car |
| 3 | Green, marked black with marker | Black car |
| 4 | Yellow | Yellow car |
| 5 | Silver | Silver car |

## Canonical game order

Use this order in the game UI and code:

1. Red
2. Blue
3. Black
4. Yellow
5. Silver

## Notes

- The green hardware button should be treated as the black button in the project.
- Do not call the third button green in the game UI.
- Use short button presses for normal gameplay.
- Avoid relying on long-press controls until the FREE-WILi hardware behavior is tested.