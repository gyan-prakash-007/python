unit = input("Is the temperature is celsius or farenheit (C/F)")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((9*temp)/5+32, 1)
    print(f"The temperature in Farenheit is : {temp}F")

elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"The temperature in Celsius is : {temp}C")

else :
    print(f"{unit} is not a valid unit")
