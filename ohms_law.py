# Adeniran, Gafar Olakunle
print("Welcome\nThis program calculates Ohms Law")
i = float(input("Enter the value of current (I): "))
r = float(input("Enter the value of resistance (R): "))

try:
    v = i * r
    print(f"Your voltage is: {v:.2f} volts")
    print("Thank you for using this program!")
    
except():
    print('You have entered a non-numerical value, pls try again')
