numbers = [2, 5, 2, 7, 2, 9]


def count_occurrences(numbers, target):
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_occurrences(numbers[1:], target)

    return count_occurrences(numbers[1:], target)


print(count_occurrences(numbers, 2))
