spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    print([food.get("name") for food in spicy_foods])
    return [food.get("name") for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    print([food for food in spicy_foods if food.get("heat_level")>5])
    return [food for food in spicy_foods if food.get("heat_level")>5]
    

def print_spicy_foods(spicy_foods):
    # print([f"{food.get("name")} | {food.get("heat_level")}:🌶" for food in spicy_foods])
    for food in spicy_foods:
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶'*food.get('heat_level')}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine")==cuisine:
            print(food)
            return food
    

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level")>5:
           print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶'*food.get('heat_level')}")
    pass

def get_average_heat_level(spicy_foods):
    total=0
    for food in spicy_foods:
        total+=food.get("heat_level")
        avg=int(total/len(spicy_foods))
    print(avg)
    return avg

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return spicy_foods

# get_names(spicy_foods)
# get_spiciest_foods(spicy_foods)
# print_spicy_foods(spicy_foods)
# get_spicy_food_by_cuisine(spicy_foods,"Thai")
# print_spiciest_foods(spicy_foods)
# get_average_heat_level(spicy_foods)
create_spicy_food(spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })