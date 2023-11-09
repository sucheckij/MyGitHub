

# IMPORTNT INFO BOUT LITS
# - list can have any data types
# - lists are in the order and the first position start from [0]

list_example = [0,1,2,3,4,5,6]

# How to display list element indexing  it from the end
print("Indexing from the end: ",list_example[-2])

# How to reverse a list
print("Reversed list: ",list_example[::-1])

# How to extend list
#one element
list_example.append(7)
print("Extended list",list_example)
#other list
def list_extension():
    list_example.extend([8,9])
    print(list_example)


# This construction is to run program in internal or when the module is imported
if __name__ == "__main__":
    print("cos")  # that part of code is used internally
else:
    print("cos cos") #that part of code is used always when module is imported and used in different module



