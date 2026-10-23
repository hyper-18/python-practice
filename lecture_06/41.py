list = [10, 20, 30, 40]


def list_sum(list):
    if len(list) == 0:
        return 0
    return list[0]+list_sum(list[1:])


print(list_sum(list))
