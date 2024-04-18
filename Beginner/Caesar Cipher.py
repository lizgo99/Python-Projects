from art import caesar_cipher_logo as logo

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
    