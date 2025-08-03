weight = float(input("enter your weight: "))
unit = input("kilogram or pounds(k or l): ")

if unit == "k":
    weight = weight *2.205
    unit = "lbs"
    print(f"your weight is : {round(weight,3)}{unit}")

elif unit == "l":
    weight = weight/2.205
    unit = "kilograms"
    print(f"your weight is : {round(weight,3)}{unit}")

else:
    print(f"{unit}id not a valid unit")

