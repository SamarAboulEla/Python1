friends = ["Radwa", "Rim", "Sara", "Dina", "Mary", "Shaimaa", "Taghreed"]
# print all list
print(friends)
# print from 1st list item
print("friends[0] = " + friends[0])
# print from LAST list item
print("friends[-1] = " + friends[-1])
# print sub list, starting from index i
print("***Sub-list: friends[5:] = ")
# type of sublist is also a list, not a string
print(friends[5:])

# print sub list, starting from index i, up to but not including index j
print("***Sub-list [start=index i] && end=[up to but not including index j]: friends[2:4] = ")
# type of sublist is also a list, not a string
print(friends[2:4])

# modify values inside an array
friends[2] = "Omnia"
print(friends)