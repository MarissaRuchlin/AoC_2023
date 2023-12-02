def calculate_highest_product_per_game(game_data_list):
    products = []

    for game_dict in game_data_list:
        game = list(game_dict.values())[0]

        highest_per_color = {}

        for colors in game:
            for color, number in colors.items():
                if color not in highest_per_color or number > highest_per_color[color]:
                    highest_per_color[color] = number

        product = 1
        for number in highest_per_color.values():
            product *= number

        products.append(product)

    return products


def process_game_parts(game_string):
    result = {}

    game_number, colors_string = game_string.split(': ', 1)
    game_id = int(game_number.split(' ')[1])

    color_parts = colors_string.split('; ')

    color_dicts = []
    for part in color_parts:
        pairs = part.split(', ')
        color_dict = {}
        for pair in pairs:
            count, color = pair.split(' ')
            color_dict[color] = int(count)
        color_dicts.append(color_dict)

    result[game_id] = color_dicts

    return result


def process_file(filepath):
    """
    Opens the file at the given filepath and processes each line to interpret the numbers.
    """
    with open(filepath, 'r') as file:
        total = 0
        game_data = []
        for line in file:
            game_data.append(process_game_parts(line.strip()))
        result = calculate_highest_product_per_game(game_data)
        total = sum(result)
        print(f"Final total: {total}")


def main():
    """
    Main method for the script. Calls process_file with the path to the input file.
    """
    input_file = './input4.txt'
    process_file(input_file)


if __name__ == "__main__":
    main()
