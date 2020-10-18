ANIMALS = {
    "s": "sheep",
    "d": "doggo",
    "@": "cat",
    "m": "moogle",
    "c": "chocobo"
}
def explore_tile(c, row, column):
    """
    Explore a tile - if there is an animal, prints the
    location and name of the animal
    """
    if c != " ":
        print("Tile ({} , {} ) contains {}".format(column, row, ANIMALS[c]))
def explore_field(p_field):
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field.
    """
    for y in range(len(p_field)):
        for x in range(len(p_field[y])):
            explore_tile(p_field[y][x], y, x)

field = [
    [" ", "s", " ", " ", "m"],
    [" ", "d", "@", "d", " "],
    ["c", " ", "s", "d", " "]
]
explore_field(field)