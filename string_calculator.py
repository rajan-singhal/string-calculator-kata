def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    '''
    Split the string by commas, convert each value to an integer, 
    and sum them up
    '''
    numbers_list = map(int,numbers.split(',')) 
    return sum(numbers_list)