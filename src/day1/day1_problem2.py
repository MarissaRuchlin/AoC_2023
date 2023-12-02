# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
# What is the sum of all of the calibration values?

import re

numbers_as_strings = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def find_first_occurrence_in_string(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring in numbers_as_strings:
                return numbers_as_strings[substring]

    return None


def find_last_occurrence_in_string(string):
    for i in range(len(string) - 1, -1, -1):
        for j in range(i - 1, - 1, -1):
            substring = string[j:i+1]
            if substring in numbers_as_strings:
                return numbers_as_strings[substring]

    return None


def find_first_number(elements, is_reversed):
    for el in elements:
        if el.isdigit():
            return el
        else:
            if is_reversed:
                possible_num = find_last_occurrence_in_string(el)
            else:
                possible_num = find_first_occurrence_in_string(el)
        if possible_num:
            return possible_num


def get_numbers_from_line(string):
    """
    Extracts numbers from the string and interprets them according to the specified logic.
    Returns a single number based on the count of numbers in the list.
    """

    #  Break up into numbers and words
    elements = re.findall(r'\d|[a-zA-Z]+', string)

    numbers = [find_first_number(elements, False), find_first_number(reversed(elements), True)]
    # Combine the number
    selected_number = int(numbers[0] + numbers[-1])
    print(f"String: {string}, Selected number: {selected_number}")
    return selected_number


def process_file(filepath):
    """
    Opens the file at the given filepath and processes each line to interpret the numbers.
    """
    with open(filepath, 'r') as file:
        total = 0
        for line in file:
            result = get_numbers_from_line(line.strip())
            total += result
            print(f"Found: {result}, Running total: {total}")
        print(f"Final total: {total}")


def main():
    input_file = './input2.txt'
    process_file(input_file)


if __name__ == "__main__":
    main()
