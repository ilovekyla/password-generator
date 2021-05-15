import random
import string
import pyperclip

alphabet = string.ascii_letters
numbers  = string.digits
special  = string.punctuation

def gen():
	while(True):
		password = ""
		length = int(input("enter length of password: "))
		for _ in range(0, length):
			password += random.choice(alphabet + numbers + special)
			pyperclip.copy(password)

		print(password + '\n')

gen()