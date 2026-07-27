import secrets
import string


alphabet = string.ascii_letters + string.digits 

password_length = 8


password = ''.join(secrets.choice(alphabet) for i in range(password_length))

print(password)