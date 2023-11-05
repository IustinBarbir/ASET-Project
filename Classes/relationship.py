class CryptosystemParameters:
    def __init__(self, encryption_key, attack_key):
        self.encryption_key = encryption_key
        self.attack_key = attack_key

    def set_encryption_key(self, encryption_key):
        self.encryption_key = encryption_key

    def set_attack_key(self, attack_key):
        self.attack_key = attack_key


# Example usage 

crypto_parameters = CryptosystemParameters(encryption_key=3, attack_key=3)

cryptor = MessageCryptor(crypto_parameters)
cryptor.set_message("Hello, World!")
cryptor.encrypt()
print("Encrypted Message:", cryptor.encrypted_message)
decrypted_message = cryptor.decrypt()
print("Decrypted Message:", decrypted_message)

simulator = AttackSimulator(crypto_parameters)
simulator.intercept_data("Khoor, Zruog!")
simulator.simulate_attack()
print("Decrypted Data:", simulator.decrypted_data)
