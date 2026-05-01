user_name = input("What is your name? ")
print(f"Hello {user_name}, Its nice to meet you! ")

birth_year =input("What year were you born? ")

birth_year_number = int(birth_year)

age = 2026 - birth_year_number

print(f"In 2026 you will be {age} years old! ")

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")

price = float(input("What is the item price? "))

if price > 100:
    print("That is too expensive we will give you a 20% discount. ")
    new_price =  price * 0.80
    print(f"Your new price is ${new_price}. ")

else:
    print("That is the perfect price no discount needed")

temperature =  int(input("What is youre temperature! "))

if temperature > 30:
    print("It is too hot")
if temperature < 10:
    print("It is too cold! ")
else:
    print("Thats perfect, How are you feeling now! ")

