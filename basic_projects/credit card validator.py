sum_odd_digit = 0
sum_even_digit = 0

card_number = input(" Enter a credit card number #:")
card_number = card_number.replace("_", "")
card_number = card_number.replace(" ", "")

card_number = card_number[::-1]

for x in card_number[::2]:
    sum_odd_digit += int(x)

for x in card_number[1::2]:
    x = int(x)*2
    if x >=10:
        sum_even_digit += (1+(x%10))
    
    else:
        sum_even_digit += x
        
total = sum_odd_digit + sum_even_digit

if total % 10 == 0:
    print("VALID")
    
else:
    print("INVALID")
    
