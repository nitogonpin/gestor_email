from cryptography.fernet import Fernet
key = ""
clave_cifrado = ""

def generate_key() -> bytes:
    key = Fernet.generate_key()
    with open("/mnt/local/datos/keys/key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_message(message: str, key: bytes) -> bytes:
   f = Fernet(key)
   return f.encrypt(message.encode())

def decrypt_message(ciphered_text: bytes, key: bytes) -> str:
   f = Fernet(key)
   return f.decrypt(ciphered_text).decode()

# Generate a key
'''
key = generate_key()
print("Key:", key)

'''
def recuperarClave():
    with open("/mnt/local/datos/keys/key.key", "rb") as key_file:
        key = key_file.read()
    return key


# Message to encrypt and decrypt
message = "hola mundo"
clave_cifrado = recuperarClave()
mensaje_encriptado = encrypt_message(message, clave_cifrado)

print(mensaje_encriptado)

mensaje_desencriptado = decrypt_message(mensaje_encriptado, clave_cifrado)

print(mensaje_desencriptado)

