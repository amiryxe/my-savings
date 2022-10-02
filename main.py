savings = {}

print("\n")
print("Hi! Enter your saving list, I will calculate total for you")
print(
    "As long as the word 'end' is not entered for name, receiving information continues"
)
print("\n")

inputName = ""

while inputName != 'end':
    inputName = input("+   Saving name: ")
    inputValue = int(input("+   Saving value: "))
    print("\n")

print(inputName, inputValue)