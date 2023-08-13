def recursive_print(lst, index):
    if index < len(lst):
        print(lst[index])
        recursive_print(lst, index + 1)
    else:
        print("Конец списка")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recursive_print(my_list, 0)