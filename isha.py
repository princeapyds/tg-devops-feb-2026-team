numbers = []

while True:
    choice = input("Enter number? (y/n): ")
    
    if choice == "y":
        num = int(input("Enter number: "))
        numbers.append(num)
    else:
        break

print("Total =", sum(numbers))
