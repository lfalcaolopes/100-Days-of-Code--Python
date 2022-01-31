import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("What do you want to translate?: ").upper()

nato_word = [nato_dict[letters] for letters in word]

print(nato_word)
