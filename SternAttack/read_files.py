def read_public_key():
    with open('publicKey.txt', 'r') as file:
        public_key = []
        for line in file:
            row = [int(num) for num in line.split()]
            public_key.append(row)
    return public_key

def read_encrypted_message():
    with open('encryptMessage.txt', 'r') as file:
        encrypted_message = [int(line.strip()) for line in file]
    return encrypted_message
