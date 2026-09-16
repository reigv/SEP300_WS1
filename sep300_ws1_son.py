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

for t,v in phone_book.keys(),phone_book.values():
    if t == phone_book.keys():
        print(t, v)