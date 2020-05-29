action = input('to log in, type "login". to create an account, type "create". and to delete an account, type "delete". '
               )


def create_account(file="usernames + passwords.txt"):
    username = input('username: ')
    password = input('password: ')

    with open(file, 'a') as myFile:
        myFile.write(encrypt(username) + ',' + encrypt(password) + '\n')


def delete_account(file="usernames + passwords.txt"):
    account = input('which account would you like to delete? ')
    password = input("please verify your account's password: ")

    with open(file, 'r') as myFile:
        text = myFile.read()

    text = text.replace(encrypt(account) + ',' + encrypt(password), '')

    with open(file, 'w') as myFile:
        myFile.write(text)


def login(file='usernames + passwords.txt'):
    account = input('username: ')
    password = input("password: ")

    with open(file, 'r') as myFile:
        text = myFile.read()

    find_account = text.find(encrypt(account) + ',' + encrypt(password) + '\n')

    if find_account != -1:
        print('welcome, ' + account)
    else:
        print('no such user or incorrect password')


def encrypt(string):
    encrypted = ''

    for char in string:
        if char != 'r' or char != 't':
            encrypted += chr(ord(char) + 17)
        elif char == 'r':
            encrypted += 'a'
        elif char == 't':
            encrypted += 't'

    return encrypted


if action == 'create':
    create_account()
if action == 'delete':
    delete_account()
if action == 'login':
    login()
