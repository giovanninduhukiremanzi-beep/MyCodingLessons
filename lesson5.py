# --- LESSON 5: LISTS ---

# 1. Creating a list (we use square brackets [ ])
inventory = ["Sword", "Shield", "Potion"]

# 2. Printing the whole list
print(f"Your inventory: {inventory}")

# 3. Accessing one item (Remember: computers start counting at 0!)
# [0] is the first item, [1] is the second...
print(f"You are holding a: {inventory[0]}")

# 4. Adding something to the list
inventory.append("Map")
print(f"Updated inventory: {inventory}")
print("Checking your items...")
for item in inventory:
    print(f"Item found: {item}")

todo_list = ["clean", "eat", "bathe" ]

todo_list.append("chess")

for task in todo_list:
    print(f"Dont forget to {task}")