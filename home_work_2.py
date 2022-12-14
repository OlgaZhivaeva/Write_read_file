with open('Cook_book.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        number_of_ingredients = int(f.readline().strip())
        dish = []
        for i in range(number_of_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            dish.append({'ingredient_name': ingredient_name,'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book.setdefault(dish_name, dish)

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingr in cook_book[dish]:
                values = {}
                values['measure'] = ingr['measure']
                values['quantity'] = ingr['quantity'] * person_count
                if ingr['ingredient_name'] in result.keys():
                    result[ingr['ingredient_name']]['quantity'] += values['quantity']
                else:
                    result.setdefault(ingr['ingredient_name'], values)
    return result

dishes = ['Омлет', 'Фахитос']
person_count = 5
print(get_shop_list_by_dishes(dishes, person_count))
