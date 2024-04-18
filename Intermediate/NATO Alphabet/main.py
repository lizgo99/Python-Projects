import pandas

#TODO 1. Create a dictionary in this format: 
df = pandas.read_csv("Intermediate/NATO Alphabet/nato_phonetic_alphabet.csv")
{"A": "Alfa", "B": "Bravo"}
dict = {row.letter:row.code for (i, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word:")
    try:
        output_list = [dict[char.capitalize()] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()

