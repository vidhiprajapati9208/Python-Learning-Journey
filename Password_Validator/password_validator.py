password = input("enter your password:")
length_password = len(password)

if(length_password < 8):
    print("password is too short!")
elif(length_password >= 15) and ("@" in password) or ("#" in password) or ("$" in password) or ("!" in password):
    print("super strong")
elif("@" not in password) and ("#" not in password) and ("$" not in password) and ("!" not in password):
    print("Missing special character!")
else:
    print("Password successfully created!")

    