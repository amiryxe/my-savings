from itertools import count
from prettytable import PrettyTable
import locale


def intWithCommas(x):
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


locale.setlocale(locale.LC_ALL, 'en_US.utf8')

savings = {}

print("\n")
print("Hi! Enter your saving list, I will calculate total for you")
print("\n")

newStatus = ""

my_table = PrettyTable()
my_table.field_names = ["No.", "Name", "Value"]

count = 0

while newStatus != 'end':
    inputName = input("+   Saving name: ")
    inputValue = int(input("+   Saving value: "))

    count += 1

    my_table.add_row([count, inputName, inputValue])

    newStatus = input(
        "\nPress enter key to add new item or type (end) word to calc result: "
    )
    savings[inputName] = inputValue
    print("\n")

values = savings.values()

print(my_table)
print("SAVINGS RESULT: ", intWithCommas(sum(values)) + "\n")