import random

letter_table = ['q','w','e','r','t','y']
number_table = [1,2,3,4,5,6,7,8,9,0]
sign_table = ['!','@','&','?']

full_table = []
full_table.extend(letter_table)
full_table.extend(number_table)
full_table.extend(sign_table)
  print(full_table)
password = ''
password2 =''

for i in range(0,6):
    # exmple1
    a = random.randint(0,len(full_table)-1)
    password += str(full_table[a])

    #example2
    password2 += str(random.choice(full_table)).upper()

    #example3
    # - there can be used random.shuffle(x)

print(password)
print(password2)




