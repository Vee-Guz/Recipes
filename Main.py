"""File used to run program"""
import json

def main():
    recipe_list = []
    option = initial_selection()

    while option != "exit":
        while option == -1:
            option = initial_selection()

        if option == 1:
            recipe_list = create_recipe(recipe_list)
        else:
            # maybe print out the name of each recipe already made and have the user input the recipe already existing
            current_recipes(recipe_list)
            recipe_name = input("Choose a recipe: ")
            find_recipe = read_recipe(recipe_list, recipe_name)

            while find_recipe is False:
                print("\nInvalid recipe. Try again.\n")
                recipe_name = input("Choose a recipe: ")
                find_recipe = read_recipe(recipe_list, recipe_name)


        option = initial_selection()


def initial_selection():
    print("\n1) Create Recipe")
    print("2) Read Recipe")
    print("To exit, type 'exit'\n")
    user_selection = input("Enter Choice: ")
    if user_selection == "1" or user_selection == "2" or user_selection == "exit":
        try:
            int(user_selection)
            return int(user_selection)
        except ValueError:
            return user_selection
    else:
        print("Input not valid, try again.")
        return -1


def create_recipe(recipe_list):
    name_recipe = input("\nRecipe Name: ")
    measurements_recipe = input("List all measurements for recipe (seperate each measurement with comma): ")
    steps_recipe = input("List steps for recipe: ")
    recipe_python = {"name_recipe": name_recipe, "measurement_recipe": measurements_recipe, "steps_recipe": steps_recipe}
    recipe_json = json.dumps(recipe_python)
    recipe_list.append(recipe_json)
    return recipe_list


def read_recipe(recipe_list, find_recipe):
    for i in range(len(recipe_list)):
        load_recipe = json.loads(recipe_list[i])
        if load_recipe["name_recipe"] == find_recipe:
            print("\n")
            print(load_recipe["name_recipe"])
            print("\nMeasurements:")
            read_measurements(load_recipe["measurement_recipe"])
            print("\nSteps:")
            read_steps(load_recipe["steps_recipe"])
            return True
    return False

def read_measurements(measurements_string):
    measurement_line = ""

    for i in measurements_string:
        if i == ",":
            print(measurement_line.strip())
            measurement_line = ""
        else:
            measurement_line += i

    print(measurement_line.strip())


def read_steps(steps_string):
    steps_line = ""
    step_number = 1

    for i in steps_string:
        if i == ",":
            steps_line = str(step_number) + ") " + steps_line.strip()
            print(steps_line)
            step_number += 1
            steps_line = ""
        else:
            steps_line += i

    steps_line = str(step_number) + ") " + steps_line.strip()
    print(steps_line)


def current_recipes(recipe_list):
    print("\n")
    for i in range(len(recipe_list)):
        load_recipe = json.loads(recipe_list[i])
        print(load_recipe["name_recipe"])
    print("\n")








if __name__ == '__main__':
    main()

