import random

with open("words.txt") as f:
    words = f.read().split()

correct_letters = set()
wrong_letters = set()
selected_word = random.choice(words)

def lost():
    return len(wrong_letters) == 8

def won():
    return all([letter in correct_letters for letter in selected_word])

def complete():
    return won() or lost()

def get_output_letter(letter):
    return letter if letter in correct_letters else "-"

def get_display():
    return "".join([get_output_letter(letter) for letter in selected_word])

print("""WELCOME TO HANGMAN

I have thought of a word, shown with dashes below""")

while not complete():
    print(get_display())
    print(f"You have got {len(wrong_letters)} misses")
    letter = input("Enter a letter: ")
    if letter in selected_word:
        correct_letters.add(letter)
    else:
        wrong_letters.add(letter)

if won():
    print(f"You got it. It was {selected_word}")
else:
    print(f"You lost. The word was {selected_word}")
