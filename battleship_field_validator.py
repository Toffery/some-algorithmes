"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true
if it has a valid disposition of ships, false otherwise.
Argument is guaranteed to be 10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces
by targeting individual cells on his field. The ship occupies one or more cells in the grid.
Size and number of ships may differ from version to version.
In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""


def validate_battlefield(field):
    ships = {
        4: 0,
        3: 0,
        2: 0,
        1: 0
    }
    for row in range(len(field[0])):
        for col in range(len(field)):
            if field[row][col] == 1:
                try:
                    ship_size = get_ship_size(row, col, field)
                    ships[ship_size] += 1
                except ValueError:
                    return False
                # If ship size is more than 4
                except KeyError:
                    return False
    return ships[4] == 1 and ships[3] == 2 and ships[2] == 3 and ships[1] == 4


def check_sides(row, col, field):
    # If row or col is the last one
    if row == len(field) - 1 or col == len(field) - 1:
        return True
    return not (field[row + 1][col] != 0 and field[row][col + 1] != 0)


def check_corners(row, col, field):
    # If row is the last one
    if row == len(field) - 1:
        return True
    # If col is first
    if col == 0:
        return field[row + 1][col + 1] != 1
    # If col is the last one
    if col == len(field) - 1:
        return field[row + 1][col - 1] != 1
    return field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


def get_ship_size(row, col, field):
    # If this point is not valid
    if not (check_sides(row, col, field) and check_corners(row, col, field)):
        raise ValueError('Nah')
    # Show that this point is already been used
    field[row][col] = -1
    # If it's not the last one raw and point under it is 1
    if row != len(field) - 1 and field[row + 1][col] == 1:
        # Repeat and plus 1
        return 1 + get_ship_size(row + 1, col, field)
    # If it's not the last one col and point right to it is 1
    if col != len(field) - 1 and field[row][col + 1] == 1:
        # Repeat and plus 1
        return 1 + get_ship_size(row, col + 1, field)
    # If none of the above conditions, there is a submarine
    return 1
