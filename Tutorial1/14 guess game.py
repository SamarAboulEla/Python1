secret_word = "Giraffe"
guess = ""
max_attempts = 5
attempt_num = 1

while guess != secret_word and attempt_num <= max_attempts:
    guess = input("Enter the secret word: ")
    attempt_num += 1

if(guess== secret_word):
    print("Correct guess!")
else:
    print("Wrong guesses. Game over!")
