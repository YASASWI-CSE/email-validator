email = input("Enter the email: ").lower()
if "@" in email and "." in email and "gmail" in email :
    print("Valid email")
else:
    print("Invalid email")