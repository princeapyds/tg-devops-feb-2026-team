numbers = []
flag = True 
while flag:
    a = input("Do you have number y/n: ")
    if a == 'y':
        numbers.append(int(input("Enter the number: ")))
    else:
        flag = False 
print(sum(numbers))
