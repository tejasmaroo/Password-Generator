import random

print("\nWelcome to the PyPassword Genertor!\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pwlist = []

nofletters = int(input("How many letters would you like to have in our password?: "))
nofnumbers = int(input("How many numbers would you like to have in our password?: "))
nofsymbols = int(input("How many symbols would you like to have in our password?: "))

for n in range(1, nofletters + 1):
    pwlist.append(random.choice(letters))
for n in range(1, nofnumbers + 1):
    pwlist.append(random.choice(numbers))
for n in range(1, nofsymbols + 1):
    pwlist.append(random.choice(symbols))

random.shuffle(pwlist)
pw = ""
for n in pwlist:
    pw += n

print(f" \nYour password is: {pw} \n")

