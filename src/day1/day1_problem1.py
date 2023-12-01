
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
#
# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
#
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all of the calibration values? Improve the following code

import re

def interpret_numbers(string):
    """
    Extracts numbers from the string and interprets them according to the specified logic.
    Returns a single number based on the count of numbers in the list.
    """
    numbers = re.findall(r'\d', string)

    selected_number = int(numbers[0] + numbers[-1])
    print(f"String: {string}, Numbers found: {numbers}, Selected number: {selected_number}")
    return selected_number


def process_file(filepath):
    """
    Opens the file at the given filepath and processes each line to interpret the numbers.
    """
    with open(filepath, 'r') as file:
        total = 0
        for line in file:
            result = interpret_numbers(line.strip())
            total += result
            print(f"Found: {result}, Running total: {total}")
        print(f"Final total: {total}")


def main():
    """
    Main method for the script. Calls process_file with the path to the input file.
    """
    input_file = './input.txt'
    process_file(input_file)


if __name__ == "__main__":
    main()
