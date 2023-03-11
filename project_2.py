#Phone Number Checker!!!
phone_number = input("Enter a Mobile Number")

def validNumber(number):

    if len(number) != 10:
        print("Enter a 10 digit Mobile Number")
    
    if number[0] not in ['6', '7', '8', '9']:
       print("Phone Number should start with 6, 7, 8 or 9")
    
    for digit in set(number):
        if number.count(digit) > 7:
            print("A digit repeats more than 7 times")
    
    for i in range(len(number)-5):
        if len(set(number[i:i+6])) == 1:
            print("A digit appears more than 5 times in a row")
    
    return True


if validNumber(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")
