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
    measurements_ls = list_storing_info(measurements_recipe)
    steps_recipe = input("List steps for recipe: ")
    steps_ls = list_storing_info(steps_recipe)
    recipe_python = {"name_recipe": name_recipe, "measurement_recipe": measurements_ls, "steps_recipe": steps_ls}
    recipe_json = json.dumps(recipe_python)
    recipe_list.append(recipe_json)
    return recipe_list


def list_storing_info(info_string):
    info_ls = info_string.split(",")
    return info_ls


def read_recipe(recipe_list, find_recipe):
    for i in range(len(recipe_list)):
        load_recipe = json.loads(recipe_list[i])
        if load_recipe["name_recipe"] == find_recipe:
            certain_step = input("Do you want a certain step from the recipe? yes/no ")

            if certain_step == "no":
                print("\n")
                print(load_recipe["name_recipe"])
                print("\nMeasurements:")
                read_measurements(load_recipe["measurement_recipe"])
                print("\nSteps:")
                read_steps(load_recipe["steps_recipe"], 0)
                return True

            else:
                amount_steps = len(load_recipe["measurement_recipe"]) + 1
                step_number = int(input("There are " + str(amount_steps) + ". Which step do you want to see? "))
                read_steps(load_recipe["steps_recipe"], step_number)
                return True


    return False


def read_measurements(measurements_ls):
    for measure in measurements_ls:
        print(measure.strip())


def read_steps(steps_ls, search_step):
    step_number = 1
    if search_step != 0:
        steps_string = str(search_step) + ")" + steps_ls[search_step - 1]
        print(steps_string)
    else:
        for step in steps_ls:
            steps_string = str(step_number) + ") " + str(step.strip())
            step_number += 1
            print(steps_string)



def current_recipes(recipe_list):
    print("\n")
    for i in range(len(recipe_list)):
        load_recipe = json.loads(recipe_list[i])
        print(load_recipe["name_recipe"])
    print("\n")





if __name__ == '__main__':
    main()

