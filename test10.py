user = "Peanut"
pw = "1978"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == pw:
    print("Hello" , username)
elif username == user and password != pw:
    print("Wrong password")
elif username != user or password != pw:
    print("Username or Passwrod Wrong")
else:
    print("Something went wrong. Try again")