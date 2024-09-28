from cryptography.fernet import Fernet
key = ""
clave_cifrado = ""

def generate_key() -> bytes:
    """
    Generates a key that will be used to cipher and decipher messages.
    The key is stored in a file named "key.key" in the path "/mnt/local/datos/keys/".
    The key is generated with the Fernet.generate_key() method and then written to the file.
    """
    key = Fernet.generate_key()  # Generate a key with the Fernet.generate_key() method
    with open("/mnt/local/datos/keys/key.key", "wb") as key_file:  # Open the file in write binary mode
        key_file.write(key)  # Write the key to the file
    return key  # Return the key

def encrypt_message(message: str, key: bytes) -> bytes:
    """
    Encrypts a given message with a given key.
    
    Parameters:
    message (str): The message to be encrypted
    key (bytes): The key to use for encryption
    
    Returns:
    bytes: The encrypted message
    """
    # Create a Fernet object with the given key
    # The Fernet class is a simple cryptography library that uses AES-128 in CBC mode and PKCS7 padding
    # to encrypt and decrypt messages. The constructor takes a key as a parameter.
    f = Fernet(key)
    
    # Encrypt the message
    # The encrypt() method of the Fernet object takes a bytes object as a parameter and
    # returns the encrypted message as a bytes object.
    # The message needs to be encoded as bytes first with the encode() method.
    encrypted_message = f.encrypt(message.encode())
    
    # Return the encrypted message
    return encrypted_message

def decrypt_message(ciphered_text: bytes, key: bytes) -> str:
    """
    Deciphers a given ciphered text with a given key.
    
    Parameters:
    ciphered_text (bytes): The ciphered text to be decrypted
    key (bytes): The key to use for decryption
    
    Returns:
    str: The decrypted message
    """
    # Create a Fernet object with the given key
    # The Fernet class is a simple cryptography library that uses AES-128 in CBC mode and PKCS7 padding
    # to encrypt and decrypt messages. The constructor takes a key as a parameter.
    f = Fernet(key)
    
    # Decrypt the ciphered text
    # The decrypt() method of the Fernet object takes a bytes object as a parameter and
    # returns the decrypted message as a bytes object.
    decrypted_message = f.decrypt(ciphered_text)
    
    # Decode the decrypted message
    # The decrypted message is a bytes object and needs to be decoded to a string
    # with the decode() method.
    decrypted_message = decrypted_message.decode()
    
    # Return the decrypted message
    return decrypted_message

# Generate a key
'''
key = generate_key()
print("Key:", key)

'''
def recuperarClave():
    """
    This function reads the encryption key from a file.
    
    The key is stored in a file named "key.key" in the "/mnt/local/datos/keys/" directory.
    The file is opened in binary read mode ("rb") and the key is read from the file.
    The key is stored in the variable "key" and returned from the function.
    """
    # Open the file in binary read mode
    with open("/mnt/local/datos/keys/key.key", "rb") as key_file:
        # Read the key from the file
        key = key_file.read()
    
    # Return the key
    return key

message = "hola mundo"
clave_cifrado = recuperarClave()

mensaje_encriptado = encrypt_message(message, clave_cifrado)

print(mensaje_encriptado)

mensaje_desencriptado = decrypt_message(mensaje_encriptado, clave_cifrado)

print(mensaje_desencriptado)

