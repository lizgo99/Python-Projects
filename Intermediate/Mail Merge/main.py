
PLACE_HOLDER = "[name]"

with open("Intermediate/Mail Merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Intermediate/Mail Merge/Input/Letters/starting_letter.txt") as letter_file:
    text = letter_file.read()
    for name in names:
        new_text = text.replace(PLACE_HOLDER , name.strip())
        with open(f"Intermediate/Mail Merge/Output/ReadyToSend/{name}.txt" , "w") as new_letter_file:
            new_letter_file.write(new_text)
        
    
    
    