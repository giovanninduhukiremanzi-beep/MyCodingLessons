secret_number = 7
tries = 3

while True: # This means "Loop Forever"
    guess = int(input("Guess the number: "))
    
    if guess == secret_number:
        print("You won!")
        break  # <--- This kills the loop immediately
    
    tries = tries - 1
    print(f"Wrong! Tries left: {tries}")

    if tries == 0:
        print("Game Over! You ran out of tries.")
        break  # <--- This also kills the loop


