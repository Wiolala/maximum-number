'''
algorithmic description

1. Program asks about number
2. Creates a list with numbers which user will be adding, 
because no number was puted in yet, list is empty
3. Makes a while loop which runs for numbers bigger then 0
4. Adds a number which was puted by user to the list which earlier created
5. Asks about number again , until number which user is puting will be bigger than 0,
the while loop will be running
6. Choosing the bigger number from the list which created
7. Printing the biggest number
'''

num_int = int(input("Input a number: "))   

number_list = []

while num_int > 0:
        number_list.append(num_int)
        num_int = int(input("Input a number: "))   

max_int = max(number_list)

print("The maximum is", max_int) 
