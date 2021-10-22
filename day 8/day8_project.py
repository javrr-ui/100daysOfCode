from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(text, shift, direction):
    new_text = ""
    

    for letter in text:
        if letter not in alphabet:
            new_text += letter
        else:
            if direction == "encode":
                position = (alphabet.index(letter) + shift) % len(alphabet)
                new_text += alphabet[position]
            elif direction == "decode":
                position = (alphabet.index(letter) - shift) % len(alphabet)
                new_text += alphabet[position]
            else:
                print("That option does not exist")
                break
            
    
    print(f"The {direction}d text is {new_text}")
option = "yes"
while option == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    option = input("Type 'yes' if you want to go again. Otherwise type 'no'.")