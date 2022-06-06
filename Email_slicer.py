email = input("Enter Your Email: ")

index = email.index('@')

username = email[:index]
domain = email[index+1:]

print("Email Address: " , email)
print("Username: " , username)
print("Doamin Name: " , domain)
