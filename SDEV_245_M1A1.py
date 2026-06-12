# pro gramming
admin_username = "admin"
admin_password = "password" # genius

user_username = "user1"
user_password = "letmein" # let me in

while True:
    foo = input("Enter Username: ")
    if foo == admin_username:
        pswd = input(f"Enter password for {foo}: ")
        if pswd == admin_password:
            print("Welcome Admin!") # message is only accessable by the admin (theoretically)
            break

    if foo == user_username:
        pswd = input(f"Enter password for {foo}: ")
        if pswd == user_password:
            print("Welcome User.") # message is only accessable by the user. (theoretically)
            break

# This shows the confidentiality part of the CIA triad.
# this is because the messages are seperated, and if someone didn't have access
# to the source code, they'd be unable to access/know either message without having logged in
# as the user or admin. This allows a seperation, that allows confidentiality.

# It's also technically integrity, but I wouldn't say it is because
# there's no information to be right or wrong other than welcoming the user/admin
