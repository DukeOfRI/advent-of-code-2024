import collections

from helpers import read_file


def calculate_distance(input_file_name: str) -> int:
    input_file = read_file(input_file_name).split("\n")
    first_column = [int(i.split("   ")[0]) for i in input_file]
    second_column = [int(i.split("   ")[1]) for i in input_file]

    first_column.sort()
    second_column.sort()

    differences = [
        abs(first_column[i] - second_column[i]) for i in range(len(first_column))
    ]
    return sum(differences)


assert calculate_distance("example.txt") == 11
assert calculate_distance("exercise.txt") == 2057374


def calculate_similarity_score(input_file_name: str) -> int:
    input_file = read_file(input_file_name).split("\n")
    first_column = [int(i.split("   ")[0]) for i in input_file]
    second_column = [int(i.split("   ")[1]) for i in input_file]

    counter = collections.Counter(second_column)

    elements = [i * counter[i] for i in first_column]
    return sum(elements)


assert calculate_similarity_score("example.txt") == 31
assert calculate_similarity_score("exercise.txt") == 23177084
