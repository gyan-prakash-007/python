#encruption program
import random
import string

chars = " " +string.punctuation +string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f" chars: {chars}")
#print(f" key: {key}")

#ENCRUPTION

plain_text = input("enter a message to encrupt :")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original text: {plain_text}")
print(f"cipher text: {cipher_text}")

#DECRUPT

cipher_text = input("enter a message to encrupt :")
plain_text= ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"original text: {plain_text}")
