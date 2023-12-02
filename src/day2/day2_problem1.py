

def get_possible_games(game_data, total_dice):
    print(f"Exploring the possibilities of {game_data}")
    filtered_game_numbers = []

    for game in game_data:
        # Extract the game number and the list of color-dice combinations
        game_number, color_combinations = list(game.items())[0]
        valid_game = True

        # Iterate through each combination of colors and dice
        for colors in color_combinations:
            # Check if the current combination is valid (each color count is less than or equal to the total dice count)
            if not all(colors.get(color, 0) <= total_dice.get(color, 0) for color in colors):
                valid_game = False
                break

        # If the game is valid, add its number to the filtered list
        if valid_game:
            filtered_game_numbers.append(game_number)

        # Debugging print statement
        print(f"Game {game_number} is {'valid' if valid_game else 'invalid'}.")

    return sum(filtered_game_numbers)


def process_game_parts(game_string):
    print(f"I've got line {game_string}")
    result = {}

    game_number, colors_string = game_string.split(': ', 1)
    game_id = int(game_number.split(' ')[1])

    color_parts = colors_string.split('; ')

    color_dicts = []
    for part in color_parts:
        print(f"Parsing {part}")
        pairs = part.split(', ')
        color_dict = {}
        for pair in pairs:
            count, color = pair.split(' ')
            print(f"Found {count} {color}")
            color_dict[color] = int(count)
        color_dicts.append(color_dict)

    # Add the result to the main dictionary
    result[game_id] = color_dicts

    return result


def process_file(filepath):
    """
    Opens the file at the given filepath and processes each line to interpret the numbers.
    """
    with open(filepath, 'r') as file:
        total = 0
        total_dice = {'red': 12, 'green': 13, 'blue': 14}
        game_data = []
        for line in file:
            game_data.append(process_game_parts(line.strip()))
        result = get_possible_games(game_data, total_dice)
        total += result
        print(f"Found: {result}, Running total: {total}")
        print(f"Final total: {total}")


def main():
    """
    Main method for the script. Calls process_file with the path to the input file.
    """
    input_file = './input2.txt'
    process_file(input_file)


if __name__ == "__main__":
    main()
