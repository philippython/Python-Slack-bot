import json

# the function below reads the json file 
def check_birthday():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    with open('birthday.json', 'r') as dates:
        birthdates = json.load(dates)
        list_of_names = list(birthdates.keys())
        for name in list_of_names:
            print(name)
        name_lookup = input("Who's birthday do you want to look up?")
        print(birthdates.get(name_lookup, "Birthday For name not available"))

check_birthday()