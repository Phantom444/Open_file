import os


def get_cook_book(file_name):
    cook_book = {}
    with open(f'{file_name}', encoding='utf-8') as file:
        cook_list = [line.strip() for line in file]
        for i, c in enumerate(cook_list):
            if c.isdigit():
                cook_book[cook_list[i - 1]] = []
                for slice in cook_list[i + 1:i + int(c) + 1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]
                    cook_book[cook_list[i - 1]].append({'ingredient_name': ingredient_name,
                                                          'quantity': quantity,
                                                          'measure': measure})
    return cook_book


print(get_cook_book('cook_book.txt'))

def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    for key in dishes:
        if key in cooking_book.keys():
            print(key)
            for value in cooking_book[key]:
                value['quantity'] *= person_count
                print(value)

                print()
            else:
                pass
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], get_cook_book('cook_book.txt'), 2))