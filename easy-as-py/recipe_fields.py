
def get_name():
    name = raw_input("Enter a name for the recipe: ")

    while name == "":
        name = "Enter a non-empty name for the recipe: "
    
    return name

def get_category():
    category = raw_input("Enter a category for this recipe (i.e., breakfast): ")

    while category == "":
        category = raw_input("Enter a non-empty name for the recipe's category: ")
    
    return category

# preparation and cook time
def get_time(action):
    print("Enter a %s time for this recipe, in hours and minutes." % action)

    prep_time_hours = int(raw_input("Enter the number of hours (integer): ")):

    while type(prep_time_hours) != int:
        prep_time_hours = int(raw_input("Enter the number of hours as an integer: "))
    
    prep_time_minutes = int(raw_input("Enter the number of minutes (integer): "))

    while type(prep_time_minutes) != int:
        prep_time_minutes = int(raw_input("Enter the number of minutes as an integer: "))
    
    return ("%sh %sm" % (prep_time_hours, prep_time_minutes))