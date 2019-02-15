#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,+-=_@#$%^&*()<>/\[]{}~`|"\':;'

passwords = input('number of passwords? ')
passwords = int(passwords)

length = input('password length? ')
length = int(length)

print ('')
print ('Here are your passwords:')
print ('')

for p in range(passwords):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print (password)
  
