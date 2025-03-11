#Assignment1
number1 = int(input('Enter num1: '))
number2 = float(input('Enter num2: '))
sum = float(number1 + number2)
print(sum)


# #Assgnment2
p = int(input('Principal balance: '))
r = int(input('annual interest rate: '))
t = int(input('time span: '))
si=int((p*r*t)/100)
print(si)


# #Assignment3
mark=int(input('Enter the Mark: '))

if mark >= 50:
    print("Passed")
else:
    print('Failed')
    


# #Assignment4

marks = int(input('Enter Total Mark:'))

if marks>=90:
    grade = 'A'
elif marks>=80:
    grade='B'
elif marks>=70:
    grade='C'
elif marks>=60:
    grade='D'
elif marks>=50:
    grade='E'
else :
    grade='F'
print('Grade:',grade)


# #Assignment5
day = int(input('Enter a day: '))


match day:
    case 1:
        print('Sunday') 
    case 2:
        print('Monday') 
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid day') 

#Assignment6
num = int(input('Enter a number: '))
table = range(1, 11)
for n in table:
    product =int(n*num)
    print(product)







#Assignment7

x= int(input("Enter a limit: "))
sum = 0
for number in range(1, x + 1):
    if number % 2 != 0:
        sum += number  
print(sum)


#Assignment8

x=5
for i in range(1, x+1):
    for j in range(i ,i+1):
        print (j,end="") 
    print()

#Assignment9
size = int(input('Enter the size of array: '))
arr1 = []
arr2 = []

for num in range(size):
    if num <= size:
        number = int(input('Enter a number to array 1 : '))
        arr1.append(number)

for num in range(size):
    if num <= size:
        numberr = int(input('Enter a number to array 2 : '))
        arr2.append(numberr)

arr1, arr2 = arr2, arr1
print(arr1)
print(arr2)


#Assignment11

size = int(input('Enter the size of array: '))
arr = []
for i in range(size):
    num = int(input('Enter a number: '))
    arr.append(num)
print(arr)

count = 0
for n in arr:
    if n%2==0:
        count += 1
print(count)

#Assignment12
string = input('Enter the word: ')
forward = string.upper()
reverse = string[::-1]
backward = reverse.upper()

if forward == backward:
    print(f"{forward} is a palindrome")
else:
    print(f"{forward} is not a palindrome")
    
    
    
    
#Assignment13
num = int(input('Enter a number: '))

if num>1:
    for i in range(2, (num//2)+1):
        if num%2 == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(num ,"is a prime number")
else:
    print(num, "is not a prime number")
    
    
#Assignment14
def calculate_grade(written_test, lab_exams, assignments):
   
    weight_written_test = 70
    weight_lab_exams = 20
    weight_assignments = 10

    grade = (written_test * weight_written_test / 100) + \
            (lab_exams * weight_lab_exams / 100) + \
            (assignments * weight_assignments / 100)
    return grade


print("Enter the marks scored by the student:")
written_test = float(input("Written test: "))
lab_exams = float(input("Lab exams: "))
assignments = float(input("Assignments: "))


grade = calculate_grade(written_test, lab_exams, assignments)


print("Grade:",grade)
    
    
#Assignment15
def calculate_income_tax(annual_income):
    tax = 0.0

    if annual_income > 10000000:
        tax += (annual_income - 10000000) * 0.30
        annual_income = 10000000
    if annual_income > 5000000:
        tax += (annual_income - 5000000) * 0.20
        annual_income = 5000000
    if annual_income > 250000:
        tax += (annual_income - 250000) * 0.05

    return tax

annual_income = float(input("Enter the annual income: "))

tax_amount = calculate_income_tax(annual_income)

print("Income tax amount",tax_amount)






    
