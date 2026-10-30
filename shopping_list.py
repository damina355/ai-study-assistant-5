# Shopping List

shopping_list = []

while True:
    item = input("Enter an item (or type 'done' to finish): ")

    if item == "done":
        break

    shopping_list.append(item)

print("\nYour Shopping List:")

for item in shopping_list:
    print("-", item)