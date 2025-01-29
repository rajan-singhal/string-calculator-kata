import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter_end_index = numbers.index("\n")
        delimiter_section = numbers[2:delimiter_end_index]

        if delimiter_section.startswith("["):
            delimiters = re.findall(r'\[([^\]]+)\]', delimiter_section)
        else:
            delimiters = [delimiter_section]
        numbers = numbers[delimiter_end_index + 1:]
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")

    numbers_list = numbers.split(",")
    negatives = []
    numbers_to_add = []

    for num in numbers_list:
        number = int(num)
        if number < 0:
            negatives.append(number)
        elif number > 1000:
            continue
        else:
            numbers_to_add.append(number)

    if negatives:
        raise ValueError(
            f"Negative numbers are not allowed: {', '.join(map(str, negatives))}")

    return sum(map(int, numbers_to_add))
