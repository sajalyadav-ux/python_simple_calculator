```python
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

def avg(n1, n2):
    return (n1 + n2) / 2


print("===== Simple Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")

select = input("Please select the operation (1-5): ")

if select in ["1", "2", "3", "4", "5"]:
    num1 = float(input("Enter the first value: "))
    num2 = float(input("Enter the second value: "))

    if select == "1":
        print("Sum is:", add(num1, num2))

    elif select == "2":
        print("Subtraction is:", sub(num1, num2))

    elif select == "3":
        print("Multiplication is:", mul(num1, num2))

    elif select == "4":
        print("Division is:", div(num1, num2))

    elif select == "5":
        print("Average is:", avg(num1, num2))

else:
    print("Invalid operation! Please select 1 to 5.")
```
