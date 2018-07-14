from recipe_fields import *

def get_recipe_details():
    details = []

    name = get_name()
    details.append(name)

    category = get_category()
    details.append(category)

    prep_time = get_time("preparation")
    details.append(prep_time)

    cook_time = get_time("cook")
    details.append(cook_time)

    ingredients = get_ingredients()
    details.append(ingredients)

    steps = get_steps()
    details.append(steps)

    return details

def main():
    recipe_information = {}
    recipe_fields = ["name", "category", "prep_time", "cook_time", "ingredients", "steps"]

    recipe_details = get_recipe_details()
    print(recipe_details)

if __name__ == "__main__":
    main()