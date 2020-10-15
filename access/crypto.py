import base64, os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Global variables
path = ''
uiPath = ''
accessPath = ''
dbPath = ''
paths = ''

# Generates Salt and returns it (in bytes)
def saltGenerator():
    salt = os.urandom(16)           # salt 16 bytes lenght random
    return salt

# Generates 1 key
def KeyGenerator(mode: int, password: bytes):
    # Application's password 
    if mode == 1:
        salt = b'\x0c<!\xdd\xc7%\x89\xb0\xd7\x88\x01D\x81U\xa2\x03' 
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

        key = base64.urlsafe_b64encode(kdf.derive(password))
    # Encrypt and Decrypt mode
    elif mode == 2:
        salt = b'\x15\r\xcf\xed9\r7\xf53\x85\xe90\x91\x9cu\xa4'
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

        key = base64.urlsafe_b64encode(kdf.derive(password))
    else:
        print('Password:')
        password_provided = input()     # password from the user
        password = password_provided.encode()   # Makes password from string to bytes
        salt = b'\x0c<!\xdd\xc7%\x89\xb0\xd7\x88\x01D\x81U\xa2\x03'
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

        key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

# Encrypts a file
def EncryptFile(filePath: str, key: bytes):
    with open(filePath, 'rb') as f:
        data = f.read()
    f.close()
    os.remove(filePath)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    new_filePath = filePath + '.enc'
    print(new_filePath)
    
    with open(new_filePath, 'wb') as f:
        f.write(encrypted)
    f.close()

# Decrypts a file
def DecryptFile(filePath: str, key):
    with open(filePath, 'rb') as f:
        data = f.read()
    f.close()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    # Moves the data back to a file
    # new_filePath = filePath[:len(filePath)-4]
    # with open(new_filePath, 'wb') as f:
    #    f.write(decrypted)
    # f.close()

    return decrypted.decode()

# Creates hash    
def DigestSHA256(msg):
    bMSG = msg.encode()
    digest = hashes.Hash(hashes.SHA256(), backend= default_backend())
    digest.update(bMSG)
    
    return digest.finalize()

# Examples
# EncryptFile('/home/pdpm19/Universidade/Universalis/Access/acessos.csv', KeyGenerator(2, DigestSHA256('1234')))