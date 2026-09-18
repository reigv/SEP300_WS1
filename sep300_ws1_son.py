# TASK 1

for i in range(1,21):
    # print(i)
    if i % 2 == 0:
        print(f"{i} is even")



# TASK 2
k=[]
i = int(input("Enter how many Fibonacci number to display: "))

if i<=0: print('Error!!, need to be more than 0')
else: 
    for n in range(i):
        if n ==0:
            k.append(n)
        elif n ==1:
            k.append(n)
        elif n>1: k.append(k[n-1] + k[n-2])


print(k)



# TASK 3

phone_book = {
    "Alice": "416-555-1234",
    "Bob": "647-555-5678",
    "Charlie": "905-555-2468",
    "Diana": "289-555-1357",
    "Ethan": "613-555-9876"
}

name = str(input('enter the name of the you want to look for: '))

found = False


for t,v in phone_book.items():
    if t == name:
        found = True
        # print("found")
        print(v)

if found == False: print("not found")


# TASK 4

fruits = {'apple' , 'banana'}
print("options: \n" \
"1. add fruit \n" \
"2. remove fruit\n" \
"3. check added fruit\n" \
"4. exit")

choice = int(input(" your option is: "))
if choice == 1: 
    add_fruit = str(input("Pls name the fruit to add: "))
    fruits.add(add_fruit)

if choice == 2:
    remove_fruit = str(input("Pls name the fruit to remove: "))
    if remove_fruit in fruits:
        fruits.remove(remove_fruit)
    else:
        print("fruit not found")

if choice == 3:
    check_fruit = str(input("Pls name the fruit to check: "))
    if check_fruit in fruits:
        print("fruit found")
    else:
        print("fruit not found")

if choice == 4:
    print("exiting program")
    