alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    new_text = ""

    for letter in text:
        if letter not in alphabet:
            new_text += letter
        else:
            position = shift % len(alphabet)
            if direction == "encode":
                position = alphabet.index(letter) + position
            elif direction == "decode":
                position = alphabet.index(letter) - position
            else:
                print("That option does not exist")
                break
            new_text += alphabet[position]
    
    print(f"The {direction}d text is {new_text}")
    
caesar(text, shift, direction)