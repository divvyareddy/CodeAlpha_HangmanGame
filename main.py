import random
print("===== Hangman Game =====")
word_list = ["python", "apple", "computer", "school", "banana"]
secret_word = random.choice(word_list)
guessed_letters = []
chances = 6
while chances > 0:
    show_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            show_word = show_word + letter + " "
        else:
            show_word = show_word + "_ "
    print("\nWord:", show_word)
    if "_" not in show_word:
        print("\n🎉 Congratulations! You guessed the word.")
        print("The word is:", secret_word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already entered this letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct Guess!")
    else:
        chances = chances - 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)
if chances == 0:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
    