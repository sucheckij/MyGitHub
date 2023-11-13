

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

def creating_list_from_input_str():
    # type a calues separated by sign ','
    example_values = input().split(',')
    # create a list of elements that are separated using by ',' sign
    print(example_values)

# This construction is to run program in internal or when the module is imported
if __name__ == "__main__":
    print("cos")  # that part of code is used internally
else:
    print("cos cos") #that part of code is used always when module is imported and used in different module



