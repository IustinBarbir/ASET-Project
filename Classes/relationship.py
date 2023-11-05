class CryptosystemParameters:
    def __init__(self, encryption_key, attack_key):
        self.encryption_key = encryption_key
        self.attack_key = attack_key

    def set_encryption_key(self, encryption_key):
        self.encryption_key = encryption_key

    def set_attack_key(self, attack_key):
        self.attack_key = attack_key
