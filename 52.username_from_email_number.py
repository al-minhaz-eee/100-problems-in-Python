"""
 52.Extract username from a given email.
 Eg if the email is nitish24singh@gmail.com then the username
 should be nitish24singh
"""
def extrate_user_name(email):
    user = ""
    for i in email:
        if i == '@':
            break
        user += i
    return user
def extract_username(email):
    return email[0:-10]

email = "nitish24@gmail.com"
print(f"username of {email} is {extrate_user_name(email)}")
email = input("Enter your email ")
print(extract_username(email))
