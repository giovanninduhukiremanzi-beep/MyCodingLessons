# --- LESSON 3: THE FOR LOOP ---

# This tells Python to repeat the code 5 times
for i in range(5):
    print(f"This is repetition number {i + 1}")


import time

print("Initiating launch sequence...")

for count in range(10,0,-1):
    print(count)
    time.sleep(1)

print("🚀 BLAST OFF!")


# --- LESSON 3 CHALLENGE: WORD REPEATER ---

# 1. Ask the user for the word ONCE
user_word = input("Enter a word you want to repeat: ")

print("Repeating your word...")

# 2. Start the loop to run 3 times
for i in range(3):
    # This will print the word you stored in the variable above
    print(user_word)

print("Done!")

