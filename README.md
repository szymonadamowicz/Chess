# chess
## Map generation

The first stage of the task will be to generate an 8x8 board. The map includes:

1. 'k' queens deployed randomly on the map,
2. One pawn placed randomly on the map.
3. Each piece is placed in a different position. When the program is turned on, the board diagram should be displayed to the user.

## Beating verification
The program should answer the questions: Will the pawn be beaten by any of the queens?
In addition, display the positions of all queens that have the ability to beat the pawn (if any).

## Additional functions
After displaying a message with information about beating, the user of the program should be able to:

1. Draw a new position for the pawn, leaving the original arrangement of queens;
2. Remove any queen (indicating its position);
3. re-verify the beating after determining the changes.

## Notes
1. Queens can move vertically, horizontally or diagonally.
2. The maximum number of queens (k) is 5.