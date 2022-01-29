with open("./Input/Names/invited_names.txt") as data:
    names_list = data.readlines()

with open("./Input/Letters/starting_letter.txt") as data:
    blueprint = data.read()

for names in names_list:
    formatted_name = names.strip("\n")
    letter = blueprint.replace("[name]", formatted_name)

    with open(f"./Output/ReadyToSend/Letter_to_{formatted_name}", mode='w') as data:
        data.write(letter)


