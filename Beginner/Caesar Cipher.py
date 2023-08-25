logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(cipher_text, cipher_shift):
  output = ""
  for c in cipher_text:
    old_index = alphabet.index(c)
    new_index = (old_index + cipher_shift) % 26
    output += alphabet[new_index]
  print(f"Here's the {direction}d result: {output}")

def decrypt(cipher_text, cipher_shift):
  output = ""
  for c in cipher_text:
    old_index = alphabet.index(c)
    new_index = (old_index - cipher_shift) % 26
    output += alphabet[new_index]
  print(f"Here's the {direction}d result: {output}")
  
def caesar1(cipher_text,cipher_shift,cipher_direction):
    if cipher_direction == "encode":
        encrypt(cipher_text, cipher_shift)
    elif cipher_direction == "decode":
        decrypt(cipher_text, cipher_shift)
    else: print("wrong input")
    
def caesar2(cipher_text, cipher_shift, cipher_direction):
  if cipher_direction != "encode" and cipher_direction != "decode":
    print("wrong input")
    return
  output = ""
  if cipher_direction == "decode":
      cipher_shift *= -1
  for c in cipher_text:
    old_index = alphabet.index(c)
    new_index = (old_index + cipher_shift) % 26  
    output += alphabet[new_index]
  print(f"Here's the {cipher_direction}d result: {output}")
  
def caesar3(cipher_text, cipher_shift, cipher_direction):
    output = ""
    if cipher_direction == "decode":
        cipher_shift *= -1

    for c in cipher_text:
        if c in alphabet:
            old_index = alphabet.index(c)
            new_index = old_index + cipher_shift
            output += alphabet[new_index]
        else:
            output += c
    print(f"Here's the {cipher_direction}d result: {output}")
      
def caesar_loop(cipher_text,cipher_shift,cipher_direction):
  caesar3(cipher_text,cipher_shift,cipher_direction)
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar1(cipher_text=text, cipher_shift=shift, cipher_direction=direction)
  elif again == "no":
    print("Goodbye")
  else:
    print("Wrong input")
    