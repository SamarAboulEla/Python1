friends = ["Alice", "Minnie", "Dory", "Moon", "Johny"]
lucky_numbers = [31, 11, 69, 27, 45]

print(friends)
# Append items to list
# extend fn can append a list
friends.extend(lucky_numbers)
print(friends)
#reset friends list & print
friends = ["Alice", "Minnie", "Dory", "Moon", "Johny"]
print(friends)

# append fn can append a list item
friends.append("Goldilocks")
print(friends)

# insert fn can insert an item in a specific list position,
#  while pushing the rest of next list items (moved one index forward)
friends.insert(1, "Snowwhite")
print(friends)

# delete list item using remove fn
friends.remove("Goldilocks")
print(friends)
print("\"Goldilocks\" removed")

# clear fn will delete all list items
#friends.clear()
#print("friends list has been cleared")
#print(friends)

# pop fn deletes the last item in the list
print("Friends list: ")
print(friends)
print(friends.pop())
print("Friends list after pop(): ")
print(friends)

# index fn return the index of item in the list - if item is present
# or it returns ValueError if item is not in the list
#print(friends.index("Tom Hanks")) #ValueError: 'Tom Hanks' is not in list
print(friends.index("Alice"))
print("Index of \"Minnie\" in the list = " + str(friends.index("Minnie")))

# count fn returns the count of occurrences of a specific list item
friends = ["Alice", "Minnie", "Alice", "Alice", "Dory", "Moon", "Alice", "Alice"]
print(friends.count("Alice"))

print("Sorting list items - alphabetically or numerically based on item types:")
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print("The reversed list of lucky numbers is:")
print(lucky_numbers)

print("List copy:")
numbers_copy = lucky_numbers.copy()
print(numbers_copy)