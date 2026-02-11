<<<<<<< HEAD


print "Hi this is Mangesh"
(edited by Vaibhav)
=======
numbers = []
flag = True 
while flag:
    a = input("Do you have number y/n: ")
    if a == 'y':
        numbers.append(int(input("Enter the number: ")))
    else:
        flag = False 
print(sum(numbers))




>>>>>>> refs/remotes/origin/main



# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

