
def get_name():
    name = input("Enter a name for the recipe: ")

    while name == "":
        name = input("Enter a non-empty name for the recipe: ")
    
    return name

def get_category():
    category = input("Enter a category for this recipe (i.e., breakfast): ")

    while category == "":
        category = input("Enter a non-empty name for the recipe's category: ")
    
    return category

# preparation and cook time
def get_time(action):
    print("\nEnter a %s time for this recipe, in hours and minutes." % action)

    try:
        prep_time_hours = int(input("Enter the number of hours (integer): "))
    except:
        prep_time_hours = ""

    while type(prep_time_hours) != int or prep_time_hours < 0:
        try:
            prep_time_hours = int(input("Enter the number of hours (integer): "))
        except:
            prep_time_hours = -1
    
    try:
        prep_time_minutes = int(input("Enter the number of minutes (integer): "))
    except:
        prep_time_minutes = ""

    while type(prep_time_minutes) != int or prep_time_minutes < 0:
        try:
            prep_time_minutes = int(input("Enter the number of minutes (integer): "))
        except:
            prep_time_minutes = -1
    
    return ("%sh %sm" % (prep_time_hours, prep_time_minutes))

def get_ingredient(number):
    ingredient = input("Enter ingredient #%s including its amount and measurement: " % number)

    while ingredient == "":
        ingredient = input("Enter a non-empty ingredient, including its amount and measurement: ")
    
    return ingredient

def get_ingredients():
    ingredients = []
    number_of_ingredients = -1

    try:
        number_of_ingredients = int(input("\nEnter the number of ingredients as an integer: "))
    except:
        number_of_ingredients = -1
    
    while number_of_ingredients < 0:
        try:
            number_of_ingredients = int(input("Enter the number of ingredients as an integer: "))
        except:
            number_of_ingredients = -1
    
    for x in range(number_of_ingredients):
        ingredient = get_ingredient(x + 1)
        ingredients.append(ingredient)
    
    return ingredients

def get_step(number):
    step = input("Enter step #%s for this recipe: " % number)

    while step == "":
        step = input("Enter a non-empty step for this recipe: ")
    
    return step

def get_steps():
    steps = []
    number_of_ingredients = -1

    try:
        number_of_steps = int(input("\nEnter the number of steps as an integer: "))
    except:
        number_of_steps = -1
    
    while number_of_steps < 0:
        try:
            number_of_steps = int(input("Enter the number of steps as an integer: "))
        except:
            number_of_steps = -1
    
    for x in range(number_of_steps):
        step = get_step(x + 1)
        steps.append(step)
    
    return steps