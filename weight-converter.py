weight = input("What is your current weight? ")
unit = input("(K)gs or (L)bs? ")

if unit.upper() == "K":
    convert = int(weight) * 0.45
    print("Your weight in Kilograms is: " + str(convert))
elif unit.upper() == "L":
    print("Your weight in pounds is: " + str(weight))
