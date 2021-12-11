# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("input/names/invited_names.txt") as invited_names:
    invited = invited_names.readlines()
    invited = list(map(str.strip, invited))

for name in invited:
    custom_letter = letter.replace("[name]", name)
    with open(f"output/readyToSend/letter_for_{name}.txt", mode="w") as custom_file:
        custom_file.write(custom_letter)
