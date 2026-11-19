name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
state = input("Enter your state: ")
pincode = input("Enter your pincode: ")
dob = input("Enter your date of birth: ")

print("\n--- Your Details ---")
print("Name    :", name)
print("Age     :", age)
print("Gender  :", gender)
print("Phone   :", phone)
print("Email   :", email)
print("Address :", address)
print("City    :", city)
print("State   :", state)
print("Pincode :", pincode)
print("DOB     :", dob)

# Save to a file
with open("details.txt", "a") as f:
    f.write(f"{name}, {age}, {gender}, {phone}, {email}, {address}, {city}, {state}, {pincode}, {dob}\n")

print("\nDetails saved successfully!")