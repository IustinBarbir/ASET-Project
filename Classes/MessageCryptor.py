class MessageCryptor:
    def __init__(self, cryptosystem_parameters):
        self.cryptosystem_parameters = cryptosystem_parameters
        self.input_message = None
        self.encrypted_message = None

    def set_message(self, message):
        self.input_message = message

    def encrypt(self):
        if self.cryptosystem_parameters is not None:
            encrypted_message = []

            for char in self.input_message:
                encrypted_char = chr(ord(char) + self.cryptosystem_parameters.encryption_key)
                encrypted_message.append(encrypted_char)

            self.encrypted_message = ''.join(encrypted_message)

    def decrypt(self):
        decrypted_message = []

        for char in self.encrypted_message:
            decrypted_char = chr(ord(char) - self.cryptosystem_parameters.encryption_key)
            decrypted_message.append(decrypted_char)

        return ''.join(decrypted_message)
