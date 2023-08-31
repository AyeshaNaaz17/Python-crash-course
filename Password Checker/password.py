user_name = input('Enter your user name: ')
pwd = input('Enter your password: ')
pwd_length = len(pwd)
pwd_encrypt = '*' * pwd_length

print(f'{user_name}, your password {pwd_encrypt} is {pwd_length} long')