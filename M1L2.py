import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("memasukkan panjang kata sandi"))
generated_password = ""

for i in range(password_length):
    generated_password += random.choice(characters)

print("kata sandi yg di hasilkan:", generated_password)

