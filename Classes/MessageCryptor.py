class MessageCryptor:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key
        self.input_message = None
        self.encrypted_message = None

    def set_message(self, message):
        self.input_message = message

    def encrypt(self):
        encrypted_message = []  # Simplified, actual Stern's algorithm is more complex

        for char in self.input_message:
            encrypted_char = chr(ord(char) + self.encryption_key)
            encrypted_message.append(encrypted_char)

        self.encrypted_message = ''.join(encrypted_message)

    def decrypt(self):
        decrypted_message = []

        for char in self.encrypted_message:
            decrypted_char = chr(ord(char) - self.encryption_key)
            decrypted_message.append(decrypted_char)

        return ''.join(decrypted_message)

# Example usage:
cryptor = MessageCryptor(encryption_key=3)
cryptor.set_message("Hello, World!")
cryptor.encrypt()
print("Encrypted Message:", cryptor.encrypted_message)
decrypted_message = cryptor.decrypt()
print("Decrypted Message:", decrypted_message)
