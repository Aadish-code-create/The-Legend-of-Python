# Check point project: area calculator.
print("========================")
print("|  Area Calculator 📐  |")
print("========================")

print()
print("--------------")
print("|    Menu    |")
print("--------------")
print("|1. Triangle |")
print("|2. Rectangle|")
print("|3. Square   |")
print("|4. Circle   |")
print("|5. Quit     |")
print("--------------")
print()

shape = 0
while shape != 5:
  shape = int(input("Please Select shape no. from the menu: "))


  if shape == 1:
    base = int(input("\nPlease enter length of Base: "))
    height = int(input("Please enter length of Height: "))
    area = (height*base)/2
    print("\nArea: " + str(area))
  elif shape == 2:
    length = int(input("\nEnter size of length: "))
    width = int(input("Enter size of width: "))
    area = length * width
    print("\nArea: " + str(area))
  elif shape == 3:
    side = int(input("\nEnter length of Side: "))
    area = side**2
    print("\nArea: " + str(area))
  elif shape == 4:
    radius = int(input("\nEnter length of radius: "))
    area = 3.14 * radius**2
    print("\nArea: " + str(area))
  elif shape == 5:
    print("\nYou have quit.")
  else:
    print("\nInvalid Input.")

print("Thank you!")

