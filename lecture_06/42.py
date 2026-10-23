numbers = [12, 45, 7, 89, 23]


def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    max_of_rest = find_max(numbers[1:])

    if numbers[0] > max_of_rest:
        return numbers[0]
    else:
        return max_of_rest


print(find_max(numbers))
