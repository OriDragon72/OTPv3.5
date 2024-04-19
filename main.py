import os
import random
import string


def GRK(length):
  key = []

  for i in range(length):
    rk = random.choice(string.ascii_letters)
    key.append(rk)

  return ''.join(key)

#One Time Pad Encryption Function
def OTPEF (message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += chr(ord(message[i]) ^ ord(key[i]))
    return encrypted_message

#Convert to ASCII
def C2A (encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char))
    return decrypted_message

#One Time Pad Decryption Function
def OTPDF(Emessage, key):
    decrypted_message = ""
    for i in range(len(Emessage)):
        decrypted_message += chr(ord(Emessage[i]) ^ ord(key[i]))
    return decrypted_message

print("Welcome to OTPV2.34 [aka. One Time Pad: version 2.34]")
print("Would you like to encrypt or decrypt?")
ans = input("[e/d]: ")

if ans == "e":
  os.system("clear")
  print("Encrypting...\n")
  mgs = input("Enter message: ")
  k = GRK(len(mgs))
  EMGSB = OTPEF(mgs, k)
  EMGSA = C2A(EMGSB)
  print("\nEncrypted Message [Binary]: " + EMGSB)
  print("Key used: " + k)
  
elif ans == "d":
  os.system("clear")
  print("Decrypting...\n")
  Emgs = input("Enter Encrypted Message: ")
  k = input("Enter Key: ")
  DMGS = OTPDF(Emgs, k)
  print("Decrypted Message: " + DMGS)
  print("Key provided: " + k)
  
else:
  print("Invalid input")
  exit(404)
